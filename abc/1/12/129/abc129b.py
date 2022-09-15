# ABC129B

def main():
    N = int(input())
    W = list(map(int, input().split()))
    s = sum(W)
    ans = s
    for w in W:
        s -= 2*w
        ans = min(ans, abs(s))
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
