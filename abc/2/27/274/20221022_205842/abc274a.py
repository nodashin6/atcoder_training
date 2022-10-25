def main():
    A, B = map(int, input().split())
    C = rround(B, A, k=3)
    print(f'{C:.3f}')
    return

def rround(b, a=1, k=0):
    b *= 10**(k+1)
    b //= a
    b += 5
    b //= 10
    b /= 10**k
    return b

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
