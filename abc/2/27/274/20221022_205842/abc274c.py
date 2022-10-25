def main():
    N = int(input())
    A = list(map(int, input().split()))

    B = [None] * (2*N+2)
    B[1] = 0
    for i, a in enumerate(A, start=1):
        B[2*i] = B[a]+1
        B[2*i+1] = B[a]+1
    print(*B[1:], sep='\n')

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
