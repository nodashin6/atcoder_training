# ABC134C

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    B = sorted(A, reverse=True)[:2]
    for a in A:
        if a == B[0]:
            print(B[1])
        else:
            print(B[0])
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
