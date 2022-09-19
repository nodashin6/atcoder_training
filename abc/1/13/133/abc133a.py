# ABC133A

def main():
    N, A, B = list(map(int, input().split()))
    print(min(N*A, B))


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
