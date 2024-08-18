# 수 이어가기
import sys
sys.stdin = open('input.txt')

N = int(input())

max_lst =[]

for i in range(1,N+1):
    lst = [N]
    idx = 1
    lst.append(i)

    while True:
        num = lst[idx-1] - lst[idx]

        if num < 0:
            break
        lst.append(num)
        idx += 1

    if len(lst) > len(max_lst):
        max_lst = lst

print(len(max_lst))
print(*max_lst)