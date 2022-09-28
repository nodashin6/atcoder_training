def main():
    N = int(input())
    P = list(map(int, input().split()))
    sorted_P = sorted(P)

    ans = 'NO'
    if P == sorted_P:
        ans = 'YES'
    for i in range(N-1):
        for j in range(i+1, N):
            A = P.copy()
            A[i], A[j] = A[j], A[i]
            if A == sorted_P: 
                ans = 'YES'
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
