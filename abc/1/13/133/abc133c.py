# ABC133C

MOD = 2019
def main():
    L, R = map(int, input().split())
    if R-L >= 2019:
        ans = 0
    else:
        ans = 2019
        for i in range(L, R):
            for j in range(i+1, R+1):
                ans = min(ans, (i*j)%MOD)
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
