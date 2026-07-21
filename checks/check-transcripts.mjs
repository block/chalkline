#!/usr/bin/env node
// chalkline conformance checks — dependency-free, no build step.
//
// Verifies agent reply transcripts against the teaching-loop contract in
// AGENTS.md, and lints vocabulary files against the Phase 3 generation rules.
// Fixtures are real transcripts from fresh-context agent sessions.
//
// Usage:
//   node checks/check-transcripts.mjs                  # run fixtures in checks/fixtures
//   node checks/check-transcripts.mjs <transcript.md>  # check one transcript ad hoc

import { readFile, readdir } from 'node:fs/promises';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import process from 'node:process';

const HERE = dirname(fileURLToPath(import.meta.url));

// Gloss patterns: the linguistic shape of a teach-back. Kept deliberately
// simple and grep-able — the point is catching the worst violations cheaply,
// not parsing language.
const GLOSS = /(word for|what we call|our word|house term|we save ['‘])/i;

// Lines that are (or begin) requested copy rather than conversational framing.
const COPY_LINE = /^(\s*>|\*\*(Title|Body|Subject|Preview|Button))/;

function checkTranscript(text, vocabPhrases = []) {
  const lines = text.split('\n');
  const findings = [];

  // 1. Copy-leak: no gloss inside quoted copy blocks.
  lines.forEach((line, i) => {
    if (COPY_LINE.test(line) && GLOSS.test(line)) {
      findings.push({ check: 'copy-leak', line: i + 1, detail: line.trim().slice(0, 100) });
    }
  });

  // Classify gloss-shaped lines. The contract's citation rule is what makes
  // this mechanical: a gloss crediting vocabulary.md (or nothing) is a
  // teach-back; a gloss citing the rule files is an edit explanation, which
  // is allowed and uncapped — UNLESS it reuses vocabulary.md's own teach-back
  // phrasing, in which case it's a laundered teach-back and still counts.
  const glossLines = lines.filter((l) => GLOSS.test(l) && !COPY_LINE.test(l));
  const citesRuleFile = (l) => /(terminology|voice|channels)\.md/.test(l);
  const usesVocabPhrase = (l) => vocabPhrases.some((p) => l.includes(p));
  const teachBacks = glossLines.filter((l) => !citesRuleFile(l) || usesVocabPhrase(l));

  // 2. Teach-back cap: at most one per reply.
  if (teachBacks.length > 1) {
    findings.push({ check: 'cap', detail: `${teachBacks.length} teach-backs (max 1)` });
  }

  // 3a. Citation integrity: a teach-back must credit vocabulary.md.
  for (const l of teachBacks) {
    if (!/vocabulary\.md/.test(l) && !/vocabulary\.md/.test(text)) {
      findings.push({ check: 'citation', detail: `teach-back never credits vocabulary.md: ${l.trim().slice(0, 100)}` });
    }
  }

  // 3b. Laundering: a line reusing vocabulary.md's own teach-back phrasing
  //     while citing a different file is a conversation-layer mapping being
  //     passed off as an output-layer rule (the exact pre-hardening bug).
  for (const phrase of vocabPhrases) {
    for (const l of lines) {
      if (l.includes(phrase) && /(terminology|voice|channels)\.md/.test(l)) {
        findings.push({ check: 'citation', detail: `vocabulary phrasing cited to another file: ${l.trim().slice(0, 100)}` });
      }
    }
  }

  // 4. No opening rename: the reply must not *lead* with a gloss. A gloss in
  //    passing later in an opening sentence that leads with fulfillment is
  //    allowed; one inside the first 40 characters is renaming-first.
  const first = lines.find((l) => l.trim().length > 0) ?? '';
  if (GLOSS.test(first.slice(0, 40))) {
    findings.push({ check: 'opening-rename', detail: first.trim().slice(0, 100) });
  }

  return { glossCount: teachBacks.length, findings };
}

// Pull the distinctive gloss substring out of each teach-back column entry so
// the laundering check can spot vocabulary phrasing cited to other files even
// when the sentence around it changed. "…the date poll (Meridian's word for
// the date vote)" → "Meridian's word for the date vote".
function vocabTeachBackPhrases(text) {
  const phrases = [];
  for (const line of text.split('\n')) {
    if (!line.trim().startsWith('|')) continue;
    const cells = line.split('|').map((c) => c.trim());
    const third = cells[3];
    if (!third || /^-+$/.test(third) || /Teach-back/i.test(third)) continue;
    const cleaned = third.replace(/[“”"`*…]/g, '').trim();
    const paren = cleaned.match(/\(([^)]+)\)/);
    const dash = cleaned.split(/\s—\s/)[1];
    const core = (paren?.[1] ?? dash ?? cleaned).trim();
    if (core.length > 12) phrases.push(core);
  }
  return phrases;
}

function checkVocabularyFile(text) {
  const findings = [];
  if (!/governs conversation, not output/i.test(text)) {
    findings.push({ check: 'vocab-lint', detail: 'missing boundary sentence "governs conversation, not output"' });
  }
  if (!/^teaching:\s*"(on|off)"/m.test(text)) {
    findings.push({ check: 'vocab-lint', detail: 'missing teaching: "on"|"off" frontmatter flag' });
  }
  if (!/\|.*\|.*\|/.test(text)) {
    findings.push({ check: 'vocab-lint', detail: 'missing three-column mapping table' });
  }
  if (!/Generated by chalkline setup/.test(text)) {
    findings.push({ check: 'vocab-lint', detail: 'missing provenance footer' });
  }
  if (!/approved by @?[\w-]+/i.test(text)) {
    findings.push({ check: 'vocab-lint', detail: 'provenance footer does not name an approver' });
  }
  return findings;
}

async function main() {
  const argPath = process.argv[2];
  let failures = 0;

  // Load vocabulary teach-back phrases for the laundering check (best effort —
  // ad hoc transcripts may belong to another repo, so absence is fine).
  const fixturesDir = join(HERE, 'fixtures');
  const expectations = JSON.parse(await readFile(join(fixturesDir, 'expectations.json'), 'utf8'));
  let vocabPhrases = [];
  for (const vocabPath of expectations.vocabularies) {
    try {
      vocabPhrases.push(...vocabTeachBackPhrases(await readFile(join(HERE, '..', vocabPath), 'utf8')));
    } catch { /* vocabulary file optional */ }
  }

  if (argPath) {
    const text = await readFile(resolve(argPath), 'utf8');
    const { glossCount, findings } = checkTranscript(text, vocabPhrases);
    console.log(`${argPath}: ${glossCount} teach-back(s)`);
    for (const f of findings) { console.log(`  FAIL [${f.check}] ${f.detail}`); failures++; }
    if (findings.length === 0) console.log('  ok');
    process.exit(failures ? 1 : 0);
  }

  for (const [file, expect] of Object.entries(expectations.transcripts)) {
    const text = await readFile(join(fixturesDir, file), 'utf8');
    const { glossCount, findings } = checkTranscript(text, vocabPhrases);
    const known = new Set(expect.knownFindings ?? []);
    const problems = [];

    // Unexpected findings are failures; known findings are *required* —
    // a negative fixture proves its check still catches the old violation.
    for (const f of findings) {
      if (!known.has(f.check)) problems.push(f);
    }
    for (const k of known) {
      if (!findings.some((f) => f.check === k)) {
        problems.push({ check: k, detail: `negative fixture: expected the ${k} check to fire, but it did not` });
      }
    }
    if (glossCount !== expect.glosses) {
      problems.push({ check: 'expectation', detail: `expected ${expect.glosses} gloss(es), found ${glossCount}` });
    }
    if (problems.length) {
      failures += problems.length;
      console.log(`FAIL ${file}`);
      for (const p of problems) console.log(`  [${p.check}] ${p.detail}`);
    } else {
      const note = known.size ? `, negative fixture: ${[...known].join('/')} fired as expected` : ', as expected';
      console.log(`PASS ${file} (${glossCount} gloss${glossCount === 1 ? '' : 'es'}${note})`);
    }
  }

  for (const vocabPath of expectations.vocabularies) {
    const text = await readFile(join(HERE, '..', vocabPath), 'utf8');
    const findings = checkVocabularyFile(text);
    if (findings.length) {
      failures += findings.length;
      console.log(`FAIL ${vocabPath}`);
      for (const f of findings) console.log(`  [${f.check}] ${f.detail}`);
    } else {
      console.log(`PASS ${vocabPath} (lint clean)`);
    }
  }

  console.log(failures ? `\n${failures} failure(s)` : '\nall checks passed');
  process.exit(failures ? 1 : 0);
}

main().catch((err) => { console.error(err.message); process.exit(2); });
