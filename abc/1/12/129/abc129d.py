# ABC129D

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    Gh = [[0]*W for _ in range(H)]
    for w in range(W):
        dq = []
        for h in range(H):
            if S[h][w] == '.':
                dq.append(h)
            if h == H-1 or S[h][w]=='#':
                x = len(dq)
                while dq:
                    Gh[dq.pop()][w] = x

    Gw = [[0]*W for _ in range(H)]
    for h in range(H):
        dq = []
        for w in range(W):
            if S[h][w] == '.':
                dq.append(w)
            if w == W-1 or S[h][w]=='#':
                x = len(dq)
                while dq:
                    Gw[h][dq.pop()] = x

    ans = 0
    for h in range(H):
        for w in range(W):
            ans = max(ans, Gh[h][w]+Gw[h][w]-1)
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
