def main():
    N, Q = map(int, input().split())
    L = [list(map(int, input().split()))[1:] for _ in range(N)]
    for _ in range(Q):
        s, t = [x-1 for x in map(int, input().split())]
        print(L[s][t])
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
