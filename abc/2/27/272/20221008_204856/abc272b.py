def main():
    N, M = map(int, input().split())
    E = [set([i]) for i in range(N)]
    for i in range(M):
        K, *A = list(map(int, input().split()))
        A = set([a-1 for a in A])
        for a in A:
            E[a] = E[a].union(A)
    ans = 'Yes'
    for i in range(N):
        if len(E[i]) < N:
            ans = 'No'
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
