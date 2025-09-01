import sys
sys.stdin = open('input.txt')

arr = []

for _ in range(10):
    N = int(input())
    arr.append(N % 42)

print(len(set(arr)))