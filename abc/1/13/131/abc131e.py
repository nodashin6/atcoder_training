# ABC131E

def main():
    N, K = map(int, input().split())
    k = (N-1)*(N-2)//2
    ans = [[i+1, N] for i in range(N-1)]
    if K <= k:
        for i in range(N-2):
            for j in range(i+1, N-1):
                if k > K:
                    ans.append([i+1, j+1])
                    k -= 1
        print(len(ans))
        for u, v in ans:
            print(u, v)
    else:
        print(-1)
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
