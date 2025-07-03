import sys
sys.stdin = open('input.txt')

N, K = map(int,input().split())

countries = []

for _ in range(N):
    lst = list(map(int,input().split()))
    countries.append(lst)

countries.sort(key = lambda x: (-x[1], -x[2], -x[3]))
rank = 1
same = 1
rank_dict = {countries[0][0] : 1}
prev = countries[0][1:]

for i in range(1,N):
    cur = countries[i][1:]

    if cur == prev:
        same += 1
        rank_dict[countries[i][0]] = rank
    else:
        rank += same
        rank_dict[countries[i][0]] = rank
        same = 1
        prev = cur

print(countries)
print(rank_dict[K])