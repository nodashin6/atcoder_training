# ABC132A

def main():
    S = input()
    ans = 'Yes'
    for s in S:
        if S.count(s) != 2:
            ans = 'No'
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
