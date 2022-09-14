# ABC128D

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = float('-inf')
    for i in range(min(K+1, N+1)):
        for j in range(i+1):
            X = V[:j]
            if i-j > 0:
                X += V[-(i-j):]
            X.sort(reverse=True)
            for k in range(K-i):
                if X and X[-1] < 0:
                    X.pop()
                else:
                    break
            ans = max(ans, sum(X))
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
