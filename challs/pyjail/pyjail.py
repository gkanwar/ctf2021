print("""Welcome to PyCalc 1.0!
All the security holes are solved so enjoy a safe calculating experience.
""")

whitelist = ['print']
safe_builtins = {}
for k in dir(__builtins__):
    if k in whitelist:
        safe_builtins[k] = __builtins__.__dict__[k]
safe_globals = {'__builtins__': safe_builtins}

while True:
    try:
        cmd = input("$ ")
        exec(f'print({cmd})', safe_globals, {})
    except Exception as e:
        print(f'Err: {e}')
