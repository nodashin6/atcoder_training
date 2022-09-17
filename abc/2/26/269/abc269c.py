# ABC269C

from itertools import product
def main():
    X = int(input())
    bits = []
    for i in range(62):
        if (X>>i)&1:
            bits.append(i)
    
    n = len(bits)
    bits = bits[::-1]
    for seq in product([0, 1], repeat=n):
        v = 0
        for i, b in zip(bits, seq):
            if b:
                v += (1<<i)
        print(v)
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
