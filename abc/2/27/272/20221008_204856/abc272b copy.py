def main():
    N, M = map(int, input().split())
    S = []
    for i in range(M):
        K, *A = list(map(int, input().split()))
        S.append(set([a-1 for a in A]))
    ans = 'Yes'
    for i in range(N-1):
        for j in range(i+1, N):
            seen = False
            for m in range(M):
                if i in S[m] and j in S[m]:
                    seen = True
            if not seen:
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
