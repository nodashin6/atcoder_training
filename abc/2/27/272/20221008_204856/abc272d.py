from collections import deque
def main():
    N, M = map(int, input().split())

    D = []
    for dx in range(-(N-1), N):
        for dy in range(-(N-1), N):
            if dx**2 + dy**2 == M:
                D.append([dx, dy])

    INF = 1<<62
    G = [[INF]*N for _ in range(N)]
    G[0][0] = 0

    dq = deque([(0, 0, 0)])
    while dq:
        t, x, y = dq.popleft()
        for dx, dy in D:
            xn = x+dx
            yn = y+dy
            if 0<=xn<N and 0<=yn<N:
                if G[xn][yn] > t+1:
                    G[xn][yn] = t+1
                    dq.append((t+1, xn, yn))

    for x in range(N):
        for y in range(N):
            if G[x][y] == INF:
                G[x][y] = -1

    for g in G:
        print(*g)
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
