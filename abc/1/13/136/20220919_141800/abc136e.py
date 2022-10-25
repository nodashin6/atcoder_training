def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 1
    D = sorted(set(search_divisor(sum(A))), reverse=True)
    for d in D:
        b = sorted([a%d for a in A])
        l = -sum(b)
        r = 0
        while b:
            bi = b.pop()
            l += bi
            r += d - bi
            if l+r == 0:
                if r <= K:
                    ans = max(ans, d)
    print(ans)
    return

# ----------------------------------------------------------------------------
# Library
import math
def search_divisor(n):
    res = []
    for i in range(1, math.floor(n**0.5 + 1)):
        if n % i == 0:
            res.append(i)
            res.append(n//i)
    return res

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
