def main():
    N, S = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0]*(S+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for x in X[i]:
            for j in range(S):
                if j + x < S+1:
                    dp[i+1][j+x] = max(dp[i+1][j+x], dp[i][j])
    
    if dp[-1][-1] == 1:
        ans = []
        v = S
        for i in reversed(range(N)):
            a, b = X[i]
            if v-a > -1 and dp[i][v-a] == 1:
                ans.append('H')
                v -= a
            else:
                ans.append('T')
                v -= b
        ans = 'Yes\n' + ''.join(ans[::-1])
    else:
        ans = 'No'
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
