def main():
    N, M = map(int, input().split())
    E = []
    for i, x in enumerate(list(map(int, input().split()))):
        E.append([x, i, N])
    for i, y in enumerate(list(map(int, input().split()))):
        E.append([y, i, N+1])
    for i in range(M):
        u, v, c = map(int, input().split())
        E.append([c, u-1, v-1])
    E = Mask.sorted(E)
    ans = min([
        UnionFind.steiner(n=N+2, edges=E, ignore_nodes=set([])),
        UnionFind.steiner(n=N+2, edges=E, ignore_nodes=set([N])),
        UnionFind.steiner(n=N+2, edges=E, ignore_nodes=set([N+1])),
        UnionFind.steiner(n=N+2, edges=E, ignore_nodes=set([N, N+1])),
    ])
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
            'left': self._id}
        self.swap = swap_methods[kind]
    
    def _swap_auto(self, x, y):
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        return x, y

    def _id(self, *args):
        return args

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

    def get_parents_size(self):
        return len(self._parents_set)

    @classmethod
    def kruskal(cls, n, edges, inf=1<<62):
        uf = cls(n=n)
        uf.cost = 0
        for c, u, v in edges:
            if not uf.same(u, v):
                uf.unite(u, v)
                uf.cost += c
                if uf.get_parents_size() == 1:
                    break
        if uf.get_parents_size() == 1:
            return uf.cost
        else:
            return inf

    @classmethod
    def steiner(cls, n, edges, ignore_nodes=set([]), inf=1<<62):
        ignore_nodes = set(ignore_nodes)
        uf = cls(n=n)
        uf._parents_set = uf._parents_set.difference(ignore_nodes)
        uf.cost = 0
        for c, u, v in edges:
            if u in ignore_nodes or v in ignore_nodes:
                continue
            if not uf.same(u, v):
                uf.unite(u, v)
                uf.cost += c
            if uf.get_parents_size() == 1:
                break
        if uf.get_parents_size() == 1:
            return uf.cost
        else:
            return inf

class Mask:
    """
    For converting list to int with bit mask.
    For examle [1, 1] is converted to 101 by twice left shit.
    """

    def __init__(self, n=30):
        """
        n : int
            [n=30] 1<<n = 2**30 > 10**9
        """
        self.n = n
        self.b = 1<<n

    def toint(self, seq):
        x, y = seq
        return (x<<self.n) + y

    def tolist(self, v):
        return (v>>self.n, v%self.b)
        
    @classmethod
    def sorted(cls, a, reverse=False):
        mask = cls(n=len(a).bit_length())
        data = [None]*len(a)
        obj = []
        for i, (ai, *other) in enumerate(a):
            data[i] = other
            obj.append(mask.toint([ai, i]))
        obj.sort(reverse=reverse)
        a_sorted = []
        for ai_masked in obj:
            ai, i = mask.tolist(ai_masked)
            a_sorted.append([ai] + data[i])
        return a_sorted

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
