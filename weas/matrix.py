#!/usr/bin/python
import sys

if len(sys.argv)==2:
    print(f"Knock, knock, {sys.argv[1]}")
else:
    sys.stderr.write(f"Usage: {sys.argv[0]} <name>\n")		
