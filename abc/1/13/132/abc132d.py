# ABC132D

MOD = 10**9 + 7
def main():
    N, K = map(int, input().split())
    R = N-K
    B = K
    nCr = MODnCr(n=2000, mod=MOD)
    for i in range(K):
        ans = nCr(B-1, i) * nCr(R+1, R-i)
        print(ans%MOD)
    return

# ----------------------------------------------------------------------------
# Library
class MODnCr():
    """
    calculation of nCr (mod P)

    Example:
    --------
    >>> ncr = MODnCr(n=2000, mod=10**9+7)
    >>> ncr(5, 2)
    10

    10 = 5!/(3!2!)
    """

    def __init__(self, n=1, mod=1_000_000_007):
        self.n = 1
        self.P = mod
        self.fac0 = [1, 1]  # n!
        self.inv0 = [0, 1]  # n^(-1)
        self.fac1 = [1, 1]  # 1/n!
        self._setup(start=2, end=n+1)

    def __call__(self, a, b):
        """
        Return
        ------
        out : int
            a!/b!(a-b)!
        """
        if b < 0 or a-b < 0:
            return 0
        if a > self.n:
            self._setup(start=self.n+1, end=a+1)
        return self.fac0[a]*self.fac1[b]*self.fac1[a-b] % self.P

    def _setup(self, start, end):

        for i in range(start, end):
            self.fac0.append(self.fac0[-1] * i % self.P)
            self.inv0.append(self.inverse(i))
            self.fac1.append(self.fac1[-1] * self.inv0[-1] % self.P)
        self.n = end-1

    def factorial(self, i):
        return self.fac0[i]

    def invfactorial(self, i):
        return self.fac1[i]

    def inverse(self, v):
        """
        a^(-1) = -(P%a)^(-1) * (P//a)    (mod P)
        """
        return - self.inv0[self.P%v] * (self.P//v) % self.P

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
