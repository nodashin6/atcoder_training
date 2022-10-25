from collections import defaultdict
import bisect

def main():
    H, W, x, y = map(int, input().split())
    x -= 1
    y -= 1
    N = int(input())

    walls = [
        defaultdict(lambda: [-1, W]),
        defaultdict(lambda: [-1, H])]
    for _ in range(N):
        r, c = [x-1 for x in map(int, input().split())]
        walls[0][r].append(c)
        walls[1][c].append(r)
    for i in range(2):
        for k in walls[i]:
            walls[i][k].sort()
    
    Q = int(input())
    ans = []
    for _ in range(Q):
        d, l = input().split()
        l = int(l)
        if d == 'U':
            if y not in walls[1]:
                walls[1][y]
            i = bisect.bisect_left(walls[1][y], x) - 1
            x = max(x-l, walls[1][y][i]+1)
        elif d == 'D':
            if y not in walls[1]:
                walls[1][y]
            i = bisect.bisect_left(walls[1][y], x)
            x = min(x+l, walls[1][y][i]-1)
        elif d == 'L':
            if x not in walls[0]:
                walls[0][x]
            i = bisect.bisect_left(walls[0][x], y) - 1
            y = max(y-l, walls[0][x][i]+1)
        elif d == 'R':
            if x not in walls[0]:
                walls[0][x]
            i = bisect.bisect_left(walls[0][x], y)
            y = min(y+l, walls[0][x][i]-1)
        ans.append([x, y])

    for x, y in ans:
        print(x+1, y+1)
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
