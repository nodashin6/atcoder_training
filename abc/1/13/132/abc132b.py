# ABC132B

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(1, N-1):
        A = sorted(P[i-1:i+2])
        if P[i] == A[1]:
            ans += 1
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
