
import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here
dthh, dtmm = input().split(" ")
tthh, ttmm = input().split(" ")
dthh = int(dthh)
dtmm = int(dtmm)
tthh = int(tthh)
ttmm = int(ttmm)

totaltravelmin = tthh*60 + ttmm

for x in range(1, totaltravelmin+1, 1):
    dtmm += 1
    if dtmm > 59:
        dtmm = 0
        dthh += 1
        if dthh > 23:
            dthh = 0

print(f"{dthh:02d}", f"{dtmm:02d}")