import sys
sys.stdin = open('input.txt')

s = str(input())

is_pelindrome = True

for i in range(len(s)//2):
    if s[i] != s[len(s)-i-1]:
        is_pelindrome = False
        break

if is_pelindrome == True:
    print(1)
else:
    print(0)