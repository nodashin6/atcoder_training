def main():
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    B = [[], []]
    for i, a in enumerate(A):
        B[i%2].append(a)

    ans= 'No'
    if is_ok(B[0][1:], X-B[0][0]) and is_ok(B[1], Y):
        ans = 'Yes'
    print(ans)
    return

def is_ok(x, k):
    dp0 = set([0])
    for xi in x:
        dp1 = set([])
        for v in dp0:
            dp1.add(v+xi)
            dp1.add(v-xi)
        dp0 = dp1
    return k in dp0


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
