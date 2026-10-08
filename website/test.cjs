const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
class Element {
  constructor() { this.textContent = ''; this.hidden = false; this.children = []; this.attributes = {}; this.listeners = {}; this.dataset = {}; }
  setAttribute(key, value) { this.attributes[key] = value; }
  append(...nodes) { this.children.push(...nodes); }
  replaceChildren(...nodes) { this.children = nodes; }
  addEventListener(event, handler) { this.listeners[event] = handler; }
  click() { this.listeners.click(); }
}
const elements = new Map();
const tasks = ['reservation', 'change'].map(task => { const el = new Element(); el.dataset.task = task; return el; });
const document = {
  getElementById(id) { if (!elements.has(id)) elements.set(id, new Element()); return elements.get(id); },
  querySelectorAll(selector) { assert.equal(selector, '[data-task]'); return tasks; },
  createElement() { return new Element(); }
};
vm.runInNewContext(fs.readFileSync(`${__dirname}/script.js`, 'utf8'), { document });
const el = id => document.getElementById(id);
for (const task of tasks) {
  task.click();
  assert.equal(task.attributes['aria-pressed'], 'true');
  assert.equal(el('draft').hidden, false);
  assert.ok(el('draft').textContent.length > 0);
  assert.match(el('overall').textContent, /Overall 1/);
  assert.ok(el('receipt-fields').children.some(row => row.children[0].textContent === 'Reviewer approval' && row.children[1].textContent === 'Not recorded.'));
  const original = el('draft').textContent;
  el('missing-toggle').click();
  assert.equal(el('draft').hidden, true);
  assert.equal(el('draft').textContent, '');
  assert.match(el('overall').textContent, /Overall 0/);
  assert.equal(el('missing-toggle').attributes['aria-pressed'], 'true');
  el('missing-toggle').click();
  assert.equal(el('draft').hidden, false);
  assert.equal(el('draft').textContent, original);
  assert.match(el('overall').textContent, /Overall 1/);
}
const html = fs.readFileSync(`${__dirname}/index.html`, 'utf8');
assert.doesNotMatch(html, /<br\b/i);
for (const match of html.matchAll(/(?:src|href)="([^"#]+)"/g)) {
  if (/^https?:/.test(match[1])) continue;
  assert.ok(fs.existsSync(`${__dirname}/${match[1]}`), `Missing local asset ${match[1]}`);
}
console.log('PASS: both tasks, blocked/restored states, approval separation, local assets, and natural wrapping.');

assert.doesNotMatch(html, /proposed work in PR #18|not a merged release|PR #18: proposed receipt work/);
assert.match(html, /docs\/traceability\.md/);
assert.match(html, /docs\/sharing-readiness\.md/);
