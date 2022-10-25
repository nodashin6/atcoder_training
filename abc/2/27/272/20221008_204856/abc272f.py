from collections import deque
import bisect
import math
def main():
    N = int(input())
    S = input()
    T = input()

    m = math.ceil(N**0.5)
    X = []
    for i in range(m):
        X.append([S[i*m:(i+1)*m], 0, i])
        X.append([T[i*m:(i+1)*m], 0, i])
    X.sort()

    for i in range(M)
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
