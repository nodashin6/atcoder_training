def main():
    a, b = map(int, input().split())
    p = [1, 2, 4]
    ans = 0
    for i in range(3):
        x = (a >> i)&1
        y = (b >> i)&1
        if x or y:
            ans += p[i]
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
