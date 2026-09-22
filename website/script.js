'use strict';
// All content is synthetic, fixed fixture data. No model, network, or storage.
const fixtures = {
  reservation: {
    label: 'Reservation request', factId: 'F1',
    facts: ['A reservation request was submitted.', 'The reservation is not confirmed.'],
    rules: ['R1 · Use “reservation request” for the submitted request.', 'R2 · Distinguish submission from confirmation. Do not add a promise or next step.'],
    draft: 'Reservation request submitted. Your reservation is not confirmed.',
    finding: 'Submission is not confirmation → factual evidence: F1; language rules: R1–R2. No next step or guarantee is added.'
  },
  change: {
    label: 'Failed change request', factId: 'F2',
    facts: ['A request to change a reservation failed.', 'The existing reservation is unchanged.', 'No cause or retry instruction was supplied.'],
    rules: ['R1 · Use “change request” for a request to change a reservation.', 'R2 · State failure and the unchanged reservation. Do not invent a cause or retry instruction.'],
    draft: 'Change request failed. Your reservation has not changed.',
    finding: 'Failure and unchanged reservation are preserved → factual evidence: F2; language rules: R1–R2. Cause and retry instructions are omitted because F2 does not supply them.'
  }
};
let selected = 'reservation';
let missing = false;
const byId = id => document.getElementById(id);
function addField(container, label, value) {
  const row = document.createElement('div');
  const term = document.createElement('dt');
  const description = document.createElement('dd');
  term.textContent = label;
  description.textContent = value;
  row.append(term, description);
  container.append(row);
}
function render() {
  const task = fixtures[selected];
  document.querySelectorAll('[data-task]').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.task === selected)));
  const toggle = byId('missing-toggle');
  toggle.setAttribute('aria-pressed', String(missing));
  toggle.textContent = `Remove required source: ${missing ? 'on' : 'off'}`;
  byId('fact-id').textContent = task.factId;
  byId('facts').replaceChildren(...task.facts.map(fact => {
    const li = document.createElement('li'); li.textContent = fact; return li;
  }));
  byId('rule-one').textContent = missing ? 'R1 · Required terminology source unavailable. Not consulted in this scenario.' : task.rules[0];
  byId('rule-two').textContent = task.rules[1];
  byId('source-status').textContent = missing ? 'Scenario: required R1 is missing; R2 remains available.' : 'Scenario: R1–R2 supplied; approval and optional calibration coverage are not established.';
  byId('draft').textContent = missing ? '' : task.draft;
  byId('draft').hidden = missing;
  byId('blocked-message').hidden = !missing;
  byId('draft-note').hidden = missing;
  byId('draft-status').textContent = missing ? 'Blocked / no draft' : 'Illustration / not approved';
  const fields = byId('receipt-fields');
  fields.replaceChildren();
  const rows = [
    ['Scope', `${task.label}, product UI, fictional Harbor ${missing ? 'requested task' : 'candidate v1'}; excludes real product use and publication approval.`],
    ['Sources', `Uncommitted synthetic fixtures in script.js#fixtures.${selected}. Facts: ${task.factId}. Language rules ${missing ? 'available: R2. R1 is missing, not consulted' : 'supplied: R1–R2'}. These labels identify in-page fixtures, not external files or verified provenance.`],
    ['Findings', missing ? `Required R1 is absent, as set by the example control. Facts ${task.factId} remain supplied; they do not replace guidance. No draft was assessed.` : task.finding],
    ['Exact wording', 'None applicable in this synthetic scenario.'],
    ['Missing evidence', `${missing ? 'Required R1 terminology source missing: blocks drafting. ' : ''}Optional calibration pair absent. Rule approval and the authority of the factual source are unconfirmed. No model or independent review was run.`],
    ['Unresolved', missing ? 'Restore the required terminology source. Rule approval and fact authority remain unconfirmed.' : 'Rule approval and factual authority remain unconfirmed; no necessary fixture fact is missing.'],
    ['Required review', 'Content reviewer: confirm rules, facts, and wording before any use. Actual owner unknown.'],
    ['Reviewer approval', 'Not recorded.']
  ];
  rows.forEach(([label, value]) => addField(fields, label, value));
  const dimensions = [
    {name: 'Guidance', score: missing ? 0 : 1, reason: missing ? 'Required terminology source unavailable.' : 'Rules supplied, not verified as approved; optional calibration pair absent.'},
    {name: 'Facts', score: 1, reason: `${task.factId} supplies the fixture claims; the source’s authority has not been confirmed.`},
    {name: 'Verification', score: 1, reason: 'This example assumes an informal reread, not a completed review or independent check.'}
  ];
  byId('scores').replaceChildren(...dimensions.map(dimension => {
    const box = document.createElement('div'); box.className = 'score';
    const title = document.createElement('strong'); title.textContent = `${dimension.name} · ${dimension.score}`;
    const reason = document.createElement('p'); reason.textContent = dimension.reason;
    box.append(title, reason); return box;
  }));
  const overall = Math.min(...dimensions.map(dimension => dimension.score));
  byId('overall').textContent = `Overall ${overall} — ${missing ? 'blocked. Required guidance is missing.' : 'limited. All three dimensions are limited.'}`;
  byId('demo-content').hidden = false;
  byId('demo-announcement').textContent = `${task.label}. Required source ${missing ? 'absent' : 'available'}. Overall ${overall}, ${missing ? 'blocked. Draft withheld.' : 'limited. Illustrative candidate shown; not approved.'}`;
}
document.querySelectorAll('[data-task]').forEach(button => button.addEventListener('click', () => { selected = button.dataset.task; render(); }));
byId('missing-toggle').addEventListener('click', () => { missing = !missing; render(); });
render();
