import bisect
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    l, r = 0, 10**12
    while r-l > 1:
        cnt = 0
        m = (l+r)//2
        for a in A:
            cnt += min(a, m)
        if cnt > K:
            r = m
        else:
            l = m
    
    cnt = 0
    B = []
    for a in A:
        if a < l:
            cnt += a
            B.append(0)
        else:
            cnt += l
            B.append(a-l)
    for i in range(N):
        if cnt == K:
            break
        if B[i] > 0:
            B[i] -= 1
            cnt += 1
    print(*B)
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
