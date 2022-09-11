# ABC126F

def main():
    """
    ans = [0, 1, 2, 3, ..., K, ..., 3, 2, 1, 0, K]
    """
    M, K = map(int, input().split())
    if M == 0 and K == 0:
        ans = [0, 0]
    elif M == 1 and K == 0:
        ans = [0, 0, 1, 1]
    elif M > 1 and K < 2**M:
        a = list(range(2**M))
        a.remove(K)
        ans = a + [K] + a[::-1] + [K]
    else:
        ans = [-1]
    print(*ans)
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
