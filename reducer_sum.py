#!/usr/bin/env python3
import sys

current_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        word, count = line.split("\t", 1)
        count = int(count)
    except ValueError:
        continue  # skip bad lines

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# print last word
if current_word:
    print(f"{current_word}\t{current_count}")
