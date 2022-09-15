# ABC129A

def main():
    P, Q, R = map(int, input().split())
    ans = sum(sorted([P, Q, R])[:2])
    print(ans)
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
