"""One Grok literature run for a prompt of this folder; only web tools.

Usage (from repo root):
  python3 investigaciones/2026-11-17-c0-causal-body-prior-art/run_grok_prompt.py <prompt.md> <suffix>

Same command and restrictions as run_grok_open.py (kept for the open run),
generalized to a chosen prompt file and output suffix. Writes
grok_<suffix>_agent.md, grok_<suffix>.jsonl, grok_<suffix>.log,
grok_<suffix>_provenance.json and informe_grok_<suffix>.md (final text after
the last tool event, unchanged). Refuses to overwrite a previous run.
"""
import datetime
import hashlib
import json
import os
import pathlib
import subprocess
import sys

root = pathlib.Path(__file__).resolve().parent
prompt_name, suffix = sys.argv[1], sys.argv[2]
parts = (root / prompt_name).read_text().split('\n---\n')
if len(parts) < 3:
    raise SystemExit('prompt needs two --- lines')
prompt = parts[1]
output = root / f'grok_{suffix}.jsonl'
if output.exists():
    raise SystemExit('Refusing to overwrite previous run')
agent = root / f'grok_{suffix}_agent.md'
agent.write_text('---\nname: targeted-literature-search\n'
                 'description: Targeted primary literature search\n---\n' + prompt)
cmd = ['grok', '--model', 'grok-4.7', '--agent', str(agent), '-p',
       'Perform the literature search and give the requested report.',
       '--tools', 'web_search,web_fetch', '--disallowed-tools', 'search_tool,use_tool,Agent',
       '--deny', 'Bash', '--deny', 'run_terminal_command', '--no-subagents',
       '--no-plan', '--max-turns', '30', '--output-format', 'streaming-json']
meta = {'prompt_file': prompt_name, 'requested_model': 'grok-4.7',
        'input_sha256': hashlib.sha256(prompt.encode()).hexdigest(), 'command': cmd,
        'started': datetime.datetime.now(datetime.timezone.utc).isoformat()}
prov = root / f'grok_{suffix}_provenance.json'
prov.write_text(json.dumps(meta, indent=2))
with output.open('w') as out, (root / f'grok_{suffix}.log').open('w') as err:
    try:
        r = subprocess.run(cmd, cwd='/tmp', env={**os.environ, 'GROK_MEMORY': '0'},
                           stdout=out, stderr=err, timeout=900)
        meta['exit_code'] = r.returncode
    except subprocess.TimeoutExpired:
        meta['exit_code'] = 'TIMEOUT'
meta['finished'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
rows = [json.loads(l) for l in output.read_text().splitlines() if l.strip()]
models = sorted({str(r.get('model') or r.get('modelUsage') or '') for r in rows} - {''})
meta['reported_model_fields'] = models[:5]
last = max((i for i, r in enumerate(rows) if r.get('type') in ('tool_call', 'tool_call_update')),
           default=-1)
body = ''.join(r.get('data', '') for r in rows[last + 1:] if r.get('type') == 'text')
(root / f'informe_grok_{suffix}.md').write_text(
    '<!-- AI output, not verified primary evidence. Requested grok-4.7; see provenance. -->\n\n'
    + body)
prov.write_text(json.dumps(meta, indent=2))
print(json.dumps(meta, indent=2))
