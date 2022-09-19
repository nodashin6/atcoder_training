# ABC131D

def main():
    N = int(input())
    mask = Mask(n=30, w=2)
    BA = []
    for _ in range(N):
        a, b = map(int, input().split())
        BA.append(mask.toint([b, a]))
    BA.sort(reverse=True)
    ans = 'Yes'
    t = 0
    while BA:
        b, a = mask.tolist(BA.pop())
        t += a
        if t > b:
            ans = 'No'
    print(ans)
    return

# ----------------------------------------------------------------------------
# Library
class Mask:
    def __init__(self, n=30, w=2):
        """
        n : int
            [n=30] 1<<n = 2**30 > 10**9
        """
        self.n = n
        self.w = w
        self.b = 1 << self.n

    def toint(self, seq):
        v = 0
        for i, x in enumerate(seq):
            n = self.n * (self.w - i - 1)
            v += x << n
        return v

    def tolist(self, v):
        seq = []
        for i in range(self.w):
            seq.append(v%self.b)
            v >>= self.n
        return seq[::-1]

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
