# ABC269F

MOD = 998244353
def main():
    N, M = map(int, input().split())
    Q = int(input())

    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        a -= 1
        b -= 1
        if (a+c)%2 == 0:
            s = fsum(a, b, c+1, d, N, M) % MOD
            t = fsum(a+1, b, c, d, N, M) % MOD
            ans = s + t
        else:
            s = fsum(a, b, c, d, N, M) % MOD
            t = fsum(a+1, b, c+1, d, N, M) % MOD
            ans = s + t
        print(ans%MOD)

    return

def fsum(a, b, c, d, N, M):
    ncol = (d-c)//2 + 1
    nrow = (b-a)//2 + 1
    vi = (a*M + c)
    s = dsum(vi, 2, ncol)
    # print(f'vi={vi}, ncol={ncol}, nrow={nrow}, s={s}')
    t = nrow*s + (nrow-1)*nrow*(M*ncol)*(2//2)
    return t % MOD

def dsum(a, d, n):
    v = (n*(2*a + (n-1)*d))//2
    return v % MOD

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
