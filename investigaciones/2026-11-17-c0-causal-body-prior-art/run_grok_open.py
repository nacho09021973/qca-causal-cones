"""One open literature run; only web tools, no repository access."""
import json, os, pathlib, subprocess, hashlib, datetime
root = pathlib.Path(__file__).resolve().parent
prompt = (root / 'prompt_abierto.md').read_text().split('\n---\n')[1]
prompt = prompt.replace('You have\nGoogle search.', 'You have web search and web fetch.')
agent = root / 'grok_open_agent.md'
agent.write_text('---\nname: open-literature-search\ndescription: Open primary literature search\n---\n' + prompt)
output = root / 'grok_open.jsonl'
if output.exists():
    raise SystemExit('Refusing to overwrite previous run')
cmd = ['grok', '--model', 'grok-4.7', '--agent', str(agent), '-p',
       'Perform the open literature search and give the requested report.',
       '--tools', 'web_search,web_fetch', '--disallowed-tools', 'search_tool,use_tool,Agent',
       '--deny', 'Bash', '--deny', 'run_terminal_command', '--no-subagents',
       '--no-plan', '--max-turns', '30', '--output-format', 'streaming-json']
metadata = {'requested_model':'grok-4.7', 'input_sha256':hashlib.sha256(prompt.encode()).hexdigest(),
            'command':cmd, 'started':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(root / 'grok_open_provenance.json').write_text(json.dumps(metadata, indent=2))
with output.open('w') as out, (root/'grok_open.log').open('w') as err:
    try:
        result = subprocess.run(cmd, cwd='/tmp', env={**os.environ,'GROK_MEMORY':'0'},
                                stdout=out, stderr=err, timeout=900)
        metadata['exit_code'] = result.returncode
    except subprocess.TimeoutExpired:
        metadata['exit_code'] = 'TIMEOUT'
metadata['finished']=datetime.datetime.now(datetime.timezone.utc).isoformat()
(root/'grok_open_provenance.json').write_text(json.dumps(metadata,indent=2))
print(json.dumps(metadata))
