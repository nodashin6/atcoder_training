# ABC134B

def main():
    N, D = map(int, input().split())
    x = 2*D+1
    ans = N//x + (N%x > 0)
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
