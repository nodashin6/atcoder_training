from collections import deque
def main():
    sm = SortedMultiset3D()
    dq = deque([])
    Q = int(input())
    for _ in range(Q):
        line = input()
        if line[0] == '1':
            _, x = map(int, line.split())
            dq.append(x)
        elif line[0] == '2':
            if sm:
                print(sm.pop(0))
            else:
                print(dq.popleft())
        elif line[0] == '3':
            while dq:
                sm.insert(dq.popleft())
    return

# ----------------------------------------------------------------------------
# Library
import sys
input = sys.stdin.readline
import math
import bisect
class SortedMultiset3D():

    def __init__(self, a=[]):

        if a:
            self._build(a)
        else:
            self.a = []
            self.size = 0
            self.sizes = [0]
            self._calc_parameter()
        # stats
        self.cnt_rebuild = 0
        self.cnt_merge = 0
        self.cnt_average = 0

    def _calc_parameter(self):

        n = len(self.a)
        self.W = max(2, math.floor(math.sqrt(n)))
        self.H = max(1, math.ceil(n/self.W))
        self.MC = max(256, n<<1)
        self.MM = self.MC >> 1
        return 

    def _build(self, a):

        a = sorted(a)
        self.size = len(a)
        K = max(2, math.ceil(math.sqrt(self.size)*0.8))
        self.a = [a[i*K:(i+1)*K] for i in range(-(-len(a)//K))]
        self._calc_parameter()
        self.sizes = self._calc_sizes()
        return

    def _calc_sizes(self):

        ss = [0] * self.H
        for i, ai in enumerate(self.a):
            ss[i//self.W] += len(ai)
        return ss

    def _rebuild(self):

        self.cnt_rebuild += 1
        self._calc_parameter()
        self.sizes = [0] * self.H
        for i in range(len(self.a)):
            self.sizes[i//self.W] += len(self.a[i])
        return


    def _merge(self):

        i = 0
        while i+1 < len(self.a):
            if len(self.a[i]) + len(self.a[i+1]) < self.MM:
                self.a[i].extend(self.a.pop(i+1))
                self.cnt_merge += 1
                continue
            i += 1
        return 

    def _average(self):
        
        for i in range(len(self.a)-1):
            if abs(len(self.a[i])-len(self.a[i+1])) > self.MM:
                tmp = self.a[i] + self.a[i+1]
                m = len(tmp)//2
                self.a[i] = tmp[:m]
                self.a[i+1] = tmp[m:]
                self.cnt_average += 1
        return 

    def insert(self, x):

        if self.a:
            i = self._bisect_row_index(x)
            bisect.insort(self.a[i], x)
            self.size += 1
            self.sizes[i//self.W] += 1
            if len(self.a[i]) > self.MC:
                self.a.insert(i+1, self.a[i][self.MM:])
                del self.a[i][self.MM:]
                self._average()
                self._rebuild()
        else:
            self.a.append([x])
            self.size += 1
            self.sizes[0] += 1
        return
    
    def pop(self, index):

        if self.a:
            if index < 0:
                index += self.size
            i, index = self._loc(index)
            if index < len(self.a[i]):
                x = self.a[i].pop(index)
                self.size -= 1
                self.sizes[i//self.W] -= 1
                if not len(self.a[i]):
                    self.a.pop(i)
                    self._merge()
                    self._rebuild()
                return x
            raise IndexError
        else:
            raise IndexError("pop from empty list")

    def discard(self, x):
        
        if self.a:
            i = self._bisect_row_index(x)
            j = bisect.bisect_left(self.a[i], x)
            if self.a[i][j] == x:
                self.a[i].pop(j)
                self.size -= 1
                self.sizes[i//self.W] -= 1
                if not len(self.a[i]):
                    self.a.pop(i)
                    self._merge()
                    self._rebuild()
        return

    def lower_bound(self, x):
        if self.a:
            i, index = 0, 0
            while i + self.W < len(self.a) and self.a[i+self.W][0] < x:
                index += self.sizes[i//self.W]
                i += self.W
            while i + 1 < len(self.a) and self.a[i+1][0] < x:
                index += len(self.a[i])
                i += 1
            return index + bisect.bisect_left(self.a[i], x)
        else:
            return None

    def gt(self, x):
        if self.a:
            i = -1
            di = max(1, len(self.a)//2)
            while di:
                while i+di < len(self.a) and self.a[i+di][-1] <= x:
                    i += di
                di >>= 1
            i = min(i+1, len(self.a)-1)
            index = bisect.bisect_right(self.a[i], x)
            if index < len(self.a[i]):
                return self.a[i][index]
        return

    def lt(self, x):
        if self.a:
            i = self._bisect_row_index(x)
            index = bisect.bisect_left(self.a[i], x) - 1
            if i > 0 and index == -1:
                i -= 1
                index += len(self.a[i])
            if 0 <= index < len(self.a[i]):
                return self.a[i][index]
        return

    def __getitem__(self, index):
        if index < 0:
            index += self.size
        i, index = self._loc(index)
        if index < len(self.a[i]):
            return self.a[i][index]
        raise IndexError

    def __len__(self):
        return self.size

    def _loc(self, index):
        i = 0
        while i + self.W < len(self.a) and index >= self.sizes[i//self.W]:
            index -= self.sizes[i//self.W]
            i += self.W
        while i + 1 < len(self.a) and index >= len(self.a[i]):
            index -= len(self.a[i])
            i += 1
        return i, index

    def _bisect_row_index(self, x):
        l, r = 0, len(self.a)
        while r-l > 1:
            m = (r+l)//2
            if (not self.a[m]) or self.a[m][0] > x:
                r = m
            else:
                l = m
        return l

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
