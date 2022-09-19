# ABC133E

from collections import deque
MOD = 10**9+7
def main():
    N, K = map(int, input().split())
    G = [set([]) for _ in range(N)]
    for _ in range(N-1):
        u, v = [x-1 for x in map(int, input().split())]
        G[u].add(v)
        G[v].add(u)

    x = 0
    seen = [None]*N
    seen[x] = [0, 0]
    ans = K
    dq = deque([x])
    while dq:
        x = dq.pop()
        for y in G[x]:
            if seen[y] is None:
                seen[y] = [1, seen[x][0]]
                seen[x][0] += 1
                dq.append(y)
                ans = max(0, ans*(K-sum(seen[y]))) % MOD
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
