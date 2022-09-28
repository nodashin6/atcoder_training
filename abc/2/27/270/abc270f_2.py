def main():
    N, M = map(int, input().split())
    
    A = [[], [], []]
    # i=0: airplane
    # i=1: ship
    # i=2: road
    for i, x in enumerate(list(map(int, input().split()))):
        A[0].append([x, i, N])
    for i, y in enumerate(list(map(int, input().split()))):
        A[1].append([y, i, N+1])
    for _ in range(M):
        u, v, c = map(int, input().split())
        A[2].append([c, u-1, v-1])
    for i in range(3):
        A[i].sort()

    ans = 1<<62
    uf00 = UnionFind(n=N+2)
    uf00.unite(0, N)
    uf00.unite(0, N+1)
    cost = kruskal(uf00, A[2])
    if cost is not None:
        ans = min(ans, cost)

    uf01 = UnionFind(n=N+2)
    uf01.unite(0, N+1)
    cost = kruskal(uf01, merge_sorted_sequence(A[0], A[2]))
    if cost is not None:
        ans = min(ans, cost)

    uf10 = UnionFind(n=N+2)
    uf10.unite(0, N)
    cost = kruskal(uf10, merge_sorted_sequence(A[1], A[2]))
    if cost is not None:
        ans = min(ans, cost)

    uf11 = UnionFind(n=N+2)
    cost = kruskal(uf11, merge_sorted_sequence(A[0], A[1], A[2]))
    if cost is not None:
        ans = min(ans, cost)

    print(ans)
    return

def kruskal(uf, a):
    uf.cost = 0
    for c, u, v in a:
        if not uf.same(u, v):
            uf.unite(u, v)
            uf.cost += c
        if len(uf.get_parents()) == 1:
            break
    if len(uf.get_parents()) == 1:
        return uf.cost
    else:
        return None
            

def merge_sorted_sequence(*args):
    a = [ai[::-1] for ai in args]
    b = []
    while a:
        x = None
        for i in range(len(a)):
            if x is None:
                x = a[i].pop()
            elif a[i][-1] < x:
                a[i-1].append(x)
                x = a[i].pop()
        for i in reversed(range(len(a))):
            if not a[i]:
                del a[i]
        b.append(x)
    return b

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
        self._parents_set = set(range(n))

    def unite(self, x, y, how='auto'):
        """
        how : str
            [left] parent of x <- parent of y
            [auto] compare the size of group of x and y  
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
        self._parents_set.remove(py)

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
