# ABC269E

# for debug
G = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1]
    ]

def main():
    N = int(input())
    l, r = 0, N
    while r-l > 1:
        m = (l+r)//2
        s = f'? 1 {m} 1 {N}'
        print(s, flush=True)
        # v = call(s)
        v = int(input())
        if v == m:
            l = m
        else:
            r = m
    h = l

    l, r = 0, N
    while r-l > 1:
        m = (l+r)//2
        s = f'? 1 {N} 1 {m}'
        print(s, flush=True)
        # v = call(s)
        v = int(input())
        if v == m:
            l = m
        else:
            r = m
    w = l
    print(f'! {h+1} {w+1}')
    return

def call(s):
    _, *line = s.split()
    a, b, c, d = [x-1 for x in map(int, line)]
    cnt = 0
    for h in range(len(G)):
        for w in range(len(G[h])):
            if a <= h <= b and c <= w <= d:
                cnt += G[h][w]
    return cnt

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
