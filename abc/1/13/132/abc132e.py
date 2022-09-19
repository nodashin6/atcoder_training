# ABC132E

from collections import deque
def main():
    N, M = map(int, input().split())
    G = [set([]) for _ in range(N)]
    for _ in range(M):
        u, v = [x-1 for x in map(int, input().split())]
        G[u].add(v)
    S, T = [x-1 for x in map(int, input().split())]

    INF = 1<<62
    dp = [[INF]*3 for _ in range(N)]
    x = S
    dp[x][2] = 0
    dq = deque([[x, 2]])
    while dq:
        x, x_st = dq.popleft()
        y_st = (x_st + 1) % 3
        dy = dp[x][x_st] + (x_st+1)//3
        for y in G[x]:
            if dy < dp[y][y_st]:
                dp[y][y_st] = dy
                dq.append([y, y_st])
    ans = dp[T][-1]
    if ans == INF:
        ans = -1
    print(ans)
    return

# ----------------------------------------------------------------------------
# Library

# ----------------------------------------------------------------------------
# INPUT
import sys
input = lambda: sys.stdin.readline().rstrip()


if __name__ == '__main__':
    try:
        f = open('./input.txt')
        input = lambda: f.readline().rstrip()
    except:
        pass
    main()
