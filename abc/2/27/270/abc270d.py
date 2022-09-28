def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0]*(N+1)
    for n in range(1, N+1):
        for i in range(K):
            if A[i] <= n:
                dp[n] = max(dp[n], n-dp[n-A[i]])
    print(dp[-1])
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
