import sys
sys.stdin = open("input.txt")

N = int(input())

if N == 0:
    print(1)
else:
    A = N 
    ans = N 

    while A > 1:
        A = A - 1 
        ans = ans * A
    
    print(ans)