# ABC128C

from itertools import product

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(M)]
    for i in range(M):
        _, *s = [x-1 for x in map(int, input().split())]
        G[i] = s
    P = list(map(int, input().split()))

    ans = 0
    for seq in product([0, 1], repeat=N):
        cnt = 0
        for i in range(M):
            if sum(seq[j] for j in G[i]) % 2 == P[i]:
                cnt += 1
        if cnt == M:
            ans += 1
    print(ans)
    return

# ----------------------------------------------------------------------------
# Library

# ----------------------------------------------------------------------------
# INPUT
import sys
input = sys.stdin.readline


if __name__ == '__main__':
    try:
        f = open('./input.txt')
        input = lambda: f.readline().rstrip()
    except:
        pass
    main()
