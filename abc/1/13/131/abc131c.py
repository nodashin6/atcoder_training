# ABC131C

import math
def main():
    A, B, C, D = map(int, input().split())
    X = C * D // math.gcd(C, D)
    ans = B-A+1
    ans -= B//C - (A-1)//C
    ans -= B//D - (A-1)//D
    ans += B//X - (A-1)//X
    print(ans)
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
