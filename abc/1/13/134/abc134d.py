def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = set([])
    for i in reversed(range(N)):
        a = A[i]
        x = 0
        for j in range(i+1, N+1, i+1):
            x += j in ans
        if x%2 != a:
            ans.add(i+1)

    if ans:
        print(len(ans))
        print(*sorted(ans))
    else:
        print(0)
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
