# ABC129E

def main():
    MOD = 10**9 + 7
    L = list(map(int, input()))
    N = len(L)
    dp1 = [[0, 0] for _ in range(N)]
    dp2 = [[0, 0] for _ in range(N)]
    dp1[0][0] = 1
    dp2[0][1] = 2
    for i in range(1, N):
        v = L[i]
        dp2[i][0] = (dp2[i-1][0] + dp2[i-1][1])
        dp2[i][1] = (dp2[i-1][0] + dp2[i-1][1]) * 2
        dp1[i][0] = (dp1[i-1][0] + dp1[i-1][1])
        dp1[i][1] = (dp1[i-1][0] + dp1[i-1][1]) * 2
        if v == 1:
            dp2[i][0] = 0
            dp1[i][0] += dp2[i-1][0] + dp2[i-1][1]
        elif v == 0:
            dp2[i][1] = 0
        dp1[i][0] %= MOD
        dp1[i][1] %= MOD
        dp2[i][0] %= MOD
        dp2[i][1] %= MOD
    ans = sum(dp1[-1] + dp2[-1]) % MOD
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
