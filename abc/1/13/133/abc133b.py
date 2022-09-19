# ABC133B

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    S = set([i**2 for i in range(1, 1000)])
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            d2 = 0
            for xik, xjk in zip(X[i], X[j]):
                d2 += (xik-xjk)**2
            if d2 in S:
                ans += 1
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
