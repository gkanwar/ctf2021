from RestrictedPython import compile_restricted, safe_builtins
from RestrictedPython.PrintCollector import PrintCollector
from flag import flag
import warnings

warnings.simplefilter("ignore")

print("""Welcome to PyCalc 2.0!
All the security holes are REALLY solved so enjoy a safe calculating experience.
""")

class PrintObj:
    def __init__(self, _getattr):
        pass
    def __call__(self):
        pass
    def _call_print(self, *args, **kwargs):
        print(*args, **kwargs)

safe_globals = {
    '__builtins__': safe_builtins,
    '_print_': PrintObj,
    '_getattr_': getattr,
    '_flag': flag
}

while True:
    try:
        cmd = input("$ ")
        byte_code = compile_restricted(f'print({cmd})', filename='<inline code>', mode='exec')
        exec(byte_code, safe_globals)
    except Exception as e:
        print(f'Err: {e}')
