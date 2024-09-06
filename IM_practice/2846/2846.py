#2846 오르막길
import sys
sys.stdin = open('input.txt')

N = int(input())  # 배열의 크기
arr = list(map(int, input().split()))  # 배열 입력

max_distance = 0  # 오르막길의 최대 거리
cont = 1  # 오르막길의 현재 길이

for i in range(1,len(arr)):
    if arr[i] > arr[i-1]:
        cont += 1

    else:
        if cont > 1:
            distance = arr[i-1] - arr[i-cont]
            if distance > max_distance:
                max_distance = distance
            cont = 1

if cont > 1:
    distance = arr[-1] - arr[-cont]
    if distance > max_distance:
        max_distance = distance

print(max_distance)


