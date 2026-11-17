"""Preserve final text after the last tool event; no scientific transformation."""
import json, pathlib
root=pathlib.Path(__file__).resolve().parent
rows=[json.loads(line) for line in (root/'grok_open.jsonl').read_text().splitlines() if line.strip()]
last=max((i for i,r in enumerate(rows) if r.get('type') in ('tool_call','tool_call_update')),default=-1)
body=''.join(r.get('data','') for r in rows[last+1:] if r.get('type')=='text')
(root/'informe_grok_abierto.md').write_text('<!-- AI output, not verified primary evidence. Model usage: grok-4.7-build; requested grok-4.7. Raw stream retained. -->\n\n'+body)
print(body)
