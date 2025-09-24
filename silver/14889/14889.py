import sys
sys.stdin = open('input.txt')

N = int(input())
S = [list(map(int,input().split())) for _ in range(N)]

min_diff = 10**9

# 팀 능력치 계산
def team_score(team):
    score = 0
    L = len(team)
    for i in range(L):
        for j in range(i+1, L):
            a, b = team[i], team[j]
            score += S[a][b] + S[b][a]
    return score

start = [0]

def dfs(idx, next_pick):
    global min_diff

    if idx == N // 2:
        start_set = set(start)
        link = [p for p in range(N) if p not in start_set]

        s1 = team_score(start)
        s2 = team_score(link)
        diff = abs(s1-s2)
        if diff < min_diff:
            min_diff = diff
        return

    for p in range(next_pick, N):
        if p in start:
            continue
        start.append(p)
        dfs(idx+1, p+1)
        start.pop()

dfs(1,1)
print(min_diff)