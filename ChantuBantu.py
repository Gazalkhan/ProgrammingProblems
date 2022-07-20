import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here
t = int(input())
for i in range(t):
    n = int(input())
    g = int(input())
    prices = list(map(int, input().split()))
    prices.sort()
    print(sum(prices[:n]))