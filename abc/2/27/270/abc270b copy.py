def main():
    x,y,z=map(int,input().split())
    print([abs(x),abs(x-z)+abs(z),-1][(x*y>y*y)<<(y*z>y*y)])
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
