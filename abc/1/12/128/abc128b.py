# ABC128B

def main():
    N = int(input())
    X = []
    for i in range(N):
        S, P = input().split()
        P = int(P)
        X.append([S, -P, i+1])
    X.sort()
    ans = [X[i][2] for i in range(N)]
    print(*ans, sep='\n')
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
