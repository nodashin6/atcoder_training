def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    S = [set([]) for _ in range(M+1)]
    for i, a in enumerate(A, start=1):
        j = 0
        if a < 0:
            j = -(a//i)
            a -= i*(a//i)
        for j in range(j, M+1):
            if a >= N:
                break
            S[j].add(a)
            a += i

    ans = []
    for i in range(1, M+1):
        for j in range(N+1):
            if j not in S[i]:
                ans.append(j)
                break
    print(*ans, sep='\n')
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
