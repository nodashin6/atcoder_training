def main():
    x, y, z = map(int, input().split())
    if x*y < y*y:
        ans = abs(x-0)
    elif y*z < y*y:
        ans = abs(x-z) + abs(z-0)
    else:
        ans = -1
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
