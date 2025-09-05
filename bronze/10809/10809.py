import sys
sys.stdin = open('input.txt')

S = input().strip()

result = [-1] * 26

for i, ch in enumerate(S):
    idx = ord(ch) - ord('a')
    if result[idx] == -1:
        result[idx] = i

print(" ".join(map(str, result)))

