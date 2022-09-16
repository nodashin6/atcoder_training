# ABC129C

def main():
    MOD = 10**9+7
    N, M = map(int, input().split())
    A = set([int(input()) for _ in range(M)])
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(N):
        for j in (1, 2):
            k = i+j
            if k not in A and k < N+1:
                dp[k] += dp[i]
                dp[k] %= MOD
    ans = dp[-1]
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
