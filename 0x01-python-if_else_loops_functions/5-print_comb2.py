#!/usr/bin/python3
for g in range(0, 100):
    if g != 99:
        print(f"{g:02d}", end=', ')
    if g == 99:
        print(f"{g:02d}")
