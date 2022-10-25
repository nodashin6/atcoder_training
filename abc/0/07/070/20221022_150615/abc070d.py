def main():
    N = int(input())
    wg = WeightedGraph(n=N, m=N-1)
    for _ in range(N-1):
        a, b, w = map(int, input().split())
        a -= 1
        b -= 1
        wg.add_egde(a, b, w)
        wg.add_egde(b, a, w)

    Q, K = map(int, input().split())
    wg.bfs(K-1)
    dist = wg.costs
    for _ in range(Q):
        x, y = map(int, input().split())
        print(dist[x-1]+dist[y-1])

    return

# ----------------------------------------------------------------------------
# Library
from collections import deque
class WeightedGraph():
    """
    Problem
    -------
    T90-13,
    """

    def __init__(self, n, m):
        """
        n: 頂点数
        m: 辺の数
        """

        self.n = n
        self.m = m
        self.G = [{} for _ in range(n)]

        self.INF = 10**15

        return

    def input(self, to_zero_index=True):

        for _ in range(self.m):
            a, b, c = map(int, input().split())
            if to_zero_index:
                a -= 1
                b -= 1
            self.G[a][b] = c
            self.G[b][a] = c

    def add_egde(self, u, v, w):

        self.G[u][v] = w
        return

    def bfs(self, x):
        """
        x: start point
        """
        
        self.costs = [self.INF]*self.n
        self.costs[x] = 0
        dq = deque([x])
        while dq:
            x = dq.popleft()
            cx = self.costs[x]
            for y, cy in self.G[x].items():
                if self.costs[y] > cx + cy:
                    self.costs[y] = cx + cy
                    dq.append(y)
        return


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
