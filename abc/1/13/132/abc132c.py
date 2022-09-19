# ABC132C

def main():
    N = int(input())
    D = list(map(int, input().split()))
    D.sort()
    m = N//2
    l, r = D[m-1], D[m]
    print(r-l)
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
