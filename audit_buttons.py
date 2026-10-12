import re, glob, os

js_funcs = set()
for j in glob.glob('js/*.js'):
    with open(j, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
        funcs = re.findall(r'(?:function\s+([a-zA-Z0-9_$]+)|(?:const|let|var)\s+([a-zA-Z0-9_$]+)\s*=\s*(?:async\s*)?(?:\([^)]*\)|[a-zA-Z0-9_$]+)\s*=>)', content)
        for f1, f2 in funcs:
            if f1: js_funcs.add(f1)
            if f2: js_funcs.add(f2)

html_files = sorted(glob.glob('*.html'))
print(f"Total JS functions found across js/*.js: {len(js_funcs)}")

standard_globals = {
    'alert', 'confirm', 'prompt', 'print', 'closeModal', 'openModal',
    'toggleMobileNav', 'closeMobileNav', 'history', 'location', 'console',
    'event', 'this', 'window', 'document', 'open', 'close', 'parseInt', 'parseFloat'
}

for h in html_files:
    with open(h, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()

    inline_scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', content, re.DOTALL)
    local_funcs = set(js_funcs) | standard_globals
    for scr in inline_scripts:
        funcs = re.findall(r'(?:function\s+([a-zA-Z0-9_$]+)|(?:const|let|var)\s+([a-zA-Z0-9_$]+)\s*=\s*(?:async\s*)?(?:\([^)]*\)|[a-zA-Z0-9_$]+)\s*=>)', scr)
        for f1, f2 in funcs:
            if f1: local_funcs.add(f1)
            if f2: local_funcs.add(f2)

    clicks = re.findall(r'onclick=["\']([^"\']+)["\']', content)
    submits = re.findall(r'onsubmit=["\']([^"\']+)["\']', content)

    unresolved = []
    for c in clicks:
        # Check first token
        m = re.match(r'([a-zA-Z0-9_$]+)\s*\(', c.strip())
        if m:
            fname = m.group(1)
            if fname not in local_funcs:
                unresolved.append(('onclick', fname, c.strip()))

    for s in submits:
        m = re.match(r'([a-zA-Z0-9_$]+)\s*\(', s.strip())
        if m:
            fname = m.group(1)
            if fname not in local_funcs:
                unresolved.append(('onsubmit', fname, s.strip()))

    if unresolved:
        print(f"\n[!] {h}: {len(unresolved)} UNRESOLVED HANDLERS (out of {len(clicks)} clicks, {len(submits)} submits):")
        for t, fn, raw in unresolved:
            print(f"    - {t}: {fn} -> {raw}")
    else:
        print(f"[OK] {h}: All {len(clicks)} clicks and {len(submits)} submits are defined.")
