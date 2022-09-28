def main():
    A, B = map(int, input().split())
    m = (A+B)//2
    if abs(A-m) == abs(B-m):
        print(m)
    else:
        print('IMPOSSIBLE')
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
