# ABC131B

def main():
    N, L = map(int, input().split())
    A = [L+i for i in range(N)]
    S = sum(A)
    ans = None
    cost = 1 << 62
    for a in A:
        if abs(a) < cost:
            cost = abs(a)
            ans = S-a
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
