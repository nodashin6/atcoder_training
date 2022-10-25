from itertools import product
from collections import Counter
def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    # meet in middle
    B0 = [Counter() for _ in range(N)]
    B1 = [Counter() for _ in range(N)]
    for seq in product([0, 1], repeat=N-1):
        h, w = 0, 0
        v = A[h][w]
        for i in seq:
            if i==1:
                h += 1
            else:
                w += 1
            v ^= A[h][w]
        B0[h][v] += 1
    for seq in product([0, 1], repeat=N-1):
        h, w = N-1, N-1
        v = A[h][w]
        for i in seq:
            if i==1:
                h -= 1
            else:
                w -= 1
            v ^= A[h][w]
        v ^= A[h][w]
        B1[h][v] += 1
    
    ans = 0
    for h, b0 in enumerate(B0):
        for v, cnt in b0.items():
            ans += cnt*B1[h][0^v]
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
