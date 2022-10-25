def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = [0]*W
    for w in range(W):
        for h in range(H):
            ans[w] += C[h][w] == '#'
    print(*ans)

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
