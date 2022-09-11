# ABC126D

def main():
    N = int(input())
    wg = WeightedGraph(n=N)
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        wg.add_egde(u-1, v-1, w)
    seen = wg.dfs(0)
    ans = [dist%2 for dist in seen]
    print(*ans, sep='\n')
    return

# ----------------------------------------------------------------------------
# Library
class WeightedGraph:

    def __init__(self, n):
        self.n = n
        self.G = [{} for _ in range(n)]

    def add_egde(self, a, b, w):
        self.G[a][b] = w
        self.G[b][a] = w

    def dfs(self, x):
        dq = [x]
        seen = [-1] * self.n
        seen[x] = 0
        while dq:
            x = dq.pop()
            for y, dxy in self.G[x].items():
                if seen[y] < 0 or seen[y] > seen[x] + dxy:
                    seen[y] = seen[x] + dxy
                    dq.append(y)
        return seen
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