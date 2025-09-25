#!/usr/bin/env python
# DOB: 05/07/2002
import sys, re
DICT_PATH = sys.argv[1] if len(sys.argv)>1 else "english_words.txt"
english = set(w.strip().lower() for w in open(DICT_PATH,encoding="utf-8",errors="ignore") if w.strip())
token_re = re.compile(r"[a-z']+")
def has_digit(s): return any(ch.isdigit() for ch in s)
for line in sys.stdin:
    for t in token_re.findall(line.lower()):
        t=t.strip("'")
        if not t or len(t)<2 or has_digit(t): 
            continue
        if t not in english:
            print(f"{t}\t1")