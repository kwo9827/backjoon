import sys
sys.stdin = open('input.txt')

N = int(input())

num = N // 4

ans = "long " * num

print(ans + "int")