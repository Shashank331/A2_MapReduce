#!/usr/bin/env python3
import sys
import re

# Read line by line from Hadoop streaming stdin
for line in sys.stdin:
    # Normalize encoding (ignore weird symbols like ΓÇ£)
    line = line.encode("utf-8", "ignore").decode("utf-8", "ignore")
    
    # Extract only alphabetic words, lowercase them
    words = re.findall(r"[a-zA-Z]+", line.lower())
    
    # Emit word and count
    for word in words:
        print(f"{word}\t1")
