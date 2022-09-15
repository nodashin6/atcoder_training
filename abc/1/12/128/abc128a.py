# ABC128A

def main():
    A, P = map(int, input().split())
    x = A*3 + P
    print(x // 2)
    return

# ----------------------------------------------------------------------------
# Library

# ----------------------------------------------------------------------------
# INPUT
import sys
input = sys.stdin.readline


if __name__ == '__main__':
    try:
        f = open('./input.txt')
        input = lambda: f.readline().rstrip()
    except:
        pass
    main()