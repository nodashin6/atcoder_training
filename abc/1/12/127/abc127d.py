# ABC127D

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    X = []
    for _ in range(M):
        B, C = map(int, input().split())
        X.append([C, B])
    X.append([0, 1<<62])
    X.sort()
    
    ans = 0
    while A:
        a = A.pop()
        c, b = X.pop()
        if c > a:
            a = c
            b -= 1
        if b > 0:
            X.append([c, b])
        ans += a
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
