import sys
sys.stdin = open('input.txt')

num = list(map(int, input().split()))

# 같은 눈 3개
if num[0] == num[1] == num[2]:
    print(10000 + num[0] * 1000)
# 같은 눈 2개 (예: 3 3 6 또는 2 5 5 또는 1 6 1)
elif num[0] == num[1] or num[0] == num[2]:
    print(1000 + num[0] * 100)
elif num[1] == num[2]:
    print(1000 + num[1] * 100)
# 모두 다른 눈
else:
    print(max(num) * 100)
