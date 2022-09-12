# ABC127C

def main():
    N, M = map(int, input().split())
    A = [0]*(10**5+2)
    for _ in range(M):
        L, R = map(int, input().split())
        A[L-1] += 1
        A[R] -= 1
    B = [0]
    for a in A:
        B.append(B[-1]+a)
    ans = B.count(M)
    print(ans)
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
