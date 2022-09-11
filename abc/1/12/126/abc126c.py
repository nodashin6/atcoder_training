# ABC126C

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        ri = 1
        while i < K:
            ri *= .5
            i *= 2
        ans += ri / N
    print(ans)
    return

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