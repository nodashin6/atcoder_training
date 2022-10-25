def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [[], []]
    for a in A:
        B[a%2].append(a)
    B[0].sort()
    B[1].sort()

    ans = -1
    if len(B[0]) > 1:
        ans = max(ans, sum(B[0][-2:]))
    if len(B[1]) > 1:
        ans = max(ans, sum(B[1][-2:]))
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
