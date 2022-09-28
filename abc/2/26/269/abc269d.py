# ABC269D

def main():
    H, W = 2005, 2005
    K = 1001

    N = int(input())
    G = [[0]*W for _ in range(H)]

    directions = [
        [-1, -1],
        [-1,  0],
        [ 0, -1],
        [ 0, +1],
        [+1,  0],
        [+1, +1]
    ]
    uf = UnionFind(n=H*W)
    for _ in range(N):
        x, y = map(int, input().split())
        x += K
        y += K
        G[x][y] = 1
        i = x*W + y
        for dx, dy in directions:
            xn = x + dx
            yn = y + dy
            if G[xn][yn] == 1:
                j = xn*W + yn
                j = uf.find(j)
                uf.unite(i, j, how='left')

    ans = 0
    for h in range(H):
        for w in range(W):
            if G[h][w] == 1:
                i = h*W + w
                if uf.parents[i] < 0:
                    ans += 1
    print(ans)
    return

# ----------------------------------------------------------------------------
# Library
class UnionFind():
    """
    Parameters:
    n : int
        size of list
    parents : int
        the parents of i-th node is `parents[i]`.
    """

    def __init__(self, n):
        
        self.n = n
        self.parents = [-1]*n

    def unite(self, x, y, how='auto'):
        """
        how : str
            left x <- y
        """
        
        if self.same(x, y):
            return
        px, py = self.find(x), self.find(y)
        if how == 'auto':
            if self.parents[px] > self.parents[py]:
                px, py = py, px
        elif how == 'left':
            pass
        self.parents[px] += self.parents[py]
        self.parents[py] = px

    def find(self, x):

        dq = []
        while self.parents[x] > -1:
            dq.append(x)
            x = self.parents[x]
        while dq:
            self.parents[dq.pop()] = x
        return x

    def same(self, x, y):

        return self.find(x) == self.find(y)

    def get_size(self, x):

        return -self.parents[self.find(x)]




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
