# ABC130D

import bisect
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0]
    for a in A:
        B.append(B[-1]+a)
    ans = 0
    for i in range(N):
        j = bisect.bisect_left(B, B[i]+K)
        ans += N-j+1
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
