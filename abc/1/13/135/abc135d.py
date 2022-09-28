P = 13
Q = 5
MOD = 10**9+7
def main():
    S = input()
    N = len(S)
    S_inv = S[::-1]
    dp = [[0]*13 for _ in range(N+1)]
    dp[0][0] = 1

    b = 1
    for i in range(N):
        if S_inv[i] == '?':
            for j in range(13):
                for k in range(10):
                    x = (b*k + j) % P
                    dp[i+1][x] += dp[i][j]
                    dp[i+1][x] %= MOD

        else:
            for j in range(13):
                k = int(S_inv[i])
                x = (b*k + j) % P
                dp[i+1][x] = dp[i][j]
                dp[i+1][x] %= MOD
                
        b *= 10
        b %= P
    print(dp[-1][Q])
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
