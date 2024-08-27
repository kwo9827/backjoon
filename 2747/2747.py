#2747 피보나치
import sys
sys.stdin = open('input.txt')

# def fibo(N):
#     if N == 1 or N == 2:
#         return 1
#
#     else:
#         num = fibo(N-1) + fibo(N-2)
#         return num

N = int(input())

arr = [0,1,1]

arr[1] = 1
arr[2] = 1

i = 2

while i < N:
    arr.append(arr[i]+arr[i-1])
    i += 1

print(arr[-1])
