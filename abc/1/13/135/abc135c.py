def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    init = sum(A)
    for i, b in enumerate(B):
        A[i] -= b
        A[i+1] += min(0, A[i])
        A[i] = max(0, A[i])
        A[i+1] = max(0, A[i+1])
    ans = init - sum(A)
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
