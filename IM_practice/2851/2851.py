#2851 슈퍼마리오
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    arr = list(map(int,input().split()))

    sum_val = 0

    for i in range(len(arr)):
        sum_val += arr[i]
        if sum_val >= 100:
            if abs(100 - sum_val) <= abs((sum_val - arr[i]) - 100):
                result = sum_val
            else:
                result = sum_val - arr[i]
            break

        else:
            result = sum_val

    print(f'#{tc} {result}')


