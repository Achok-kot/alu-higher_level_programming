#!/usr/bin/python3
for i in range(97, 123):
    if i in (101, 113):  # skip 'e' (101) and 'q' (113)
        continue
    print(f"{i:c}", end="")

