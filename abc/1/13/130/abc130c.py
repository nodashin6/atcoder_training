# ABC130C

def main():
    H, W, x, y = map(int, input().split())
    ans = H*W/2
    if H == x*2 and W == y*2:
        flg = 1
    else:
        flg = 0
    print(ans, flg)
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
