from collections import defaultdict
def main():
    INF = 1<<62
    N, M = map(int, input().split())
    
    info = defaultdict(lambda: [[], [], []])
    # info[0]: airplane
    # info[1]: ship
    # info[2]: road
    costs = set([])
    for i, x in enumerate(list(map(int, input().split()))):
        costs.add(x)
        info[x][0].append(i)
    for i, y in enumerate(list(map(int, input().split()))):
        costs.add(y)
        info[y][1].append(i)
    for _ in range(M):
        u, v, c = map(int, input().split())
        costs.add(c)
        info[c][2].append([u-1, v-1])
    costs = sorted(costs)

    uf00 = set_uf(size=N+2, default_unite=[N, N+1], allowable=set([2]))
    uf01 = set_uf(size=N+2, default_unite=[N+1], allowable=set([0, 2]))
    uf10 = set_uf(size=N+2, default_unite=[N], allowable=set([1, 2]))
    uf11 = set_uf(size=N+2, default_unite=[], allowable=set([0, 1, 2]))
    ufs = [uf00, uf01, uf10, uf11]
    for c in costs:
        for i in range(3):
            while info[c][i]:
                if i < 2:
                    u, v = info[c][i].pop(), N+i
                else:
                    u, v = info[c][i].pop()
                for uf in ufs:
                    connect(uf, u, v, c, kind=i)
    ans = 1<<62
    for uf in ufs:
        if len(uf.get_parents()) == 1:
            ans = min(ans, uf.cost)
    print(ans)
    return

def set_uf(size, default_unite=[], allowable=set([])):
    uf = UnionFind(n=size)
    for v in default_unite:
        uf.unite(0, v)
    uf.cost = 0
    uf.allowable = allowable
    return uf

def connect(uf, u, v, c, kind):
    if kind in uf.allowable:
        if not uf.same(u, v):
            uf.unite(u, v)
            uf.cost += c

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

    def __init__(self, n, kind='auto'):
        """
        kind : str
            [left] parent of x <- parent of y
            [auto] compare the size of group of x and y  
        """
        self.n = n
        self.parents = [-1]*n
        self._parents_set = set(range(n))
        swap_methods = {
            'auto': self._swap_auto,
            'left': self._swap_left}
        self.swap = swap_methods[kind]
    
    def _swap_auto(self, x, y):
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        return x, y

    def _swap_left(self, x, y):
        return x, y

    def unite(self, x, y):
        if self.same(x, y):
            return
        x, y = self.swap(self.find(x), self.find(y))
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self._parents_set.remove(y)

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
    
    def get_parents(self):
        return self._parents_set

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
