import math
from collections import deque
from itertools import product
def main():

    INF = 1<<62
    # INF = 99
    N, M = map(int, input().split())
    K = N+M
    X = [list(map(int, input().split())) for _ in range(K)]

    dq = set([])
    dq_next = set([])
    dp = [[INF]*K for _ in range(1<<K)]
    for i in range(K):
        dp[1<<i][i] = calc_dist([0, 0], X[i])
        dq.add(1<<i)
    # print(*dp, sep='\n')

    dq = list(dq)
    while dq:
        s = dq.pop()
        
        speed = 1
        for m in range(M):
            speed <<= (s>>(K-m-1))&1

        # print(f'now state: {s:0{K}b}, speed: {speed}')
        for x in range(K):
            if s>>x & 1 == 0:
                continue
            for y in range(K):
                if s>>y & 1:
                    continue
                sn = s + (1<<y)
                dq_next.add(sn)
                dist = calc_dist(X[x], X[y])

                time = dist/speed
                if dp[sn][y] > dp[s][x] + time:
                    dp[sn][y] = dp[s][x] + time
                    # print(f'state: {s:0{K}b}[{x}]->{sn:0{K}b} time: {dp[sn][y]}')

        if not dq:
            dq = list(dq_next)
            dq_next = set([])

    ans = INF
    for s in range(1<<K):
        if s % (1<<N) == (1<<N) - 1:
            pass
            # print(s, f'{s:0{K}b}')
            # print(f'dp[{s}]: {dp[s]}')
        else:
            continue
        speed = 1
        for m in range(M):
            speed <<= (s>>(K-m-1))&1
        for x in range(K):
            dist = calc_dist(X[x], [0, 0])
            time = dist / speed
            ans = min(ans, dp[s][x]+time)
    print(ans)
    return

def calc_dist(pos0, pos1):
    x0, y0 = pos0
    x1, y1 = pos1
    return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)

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