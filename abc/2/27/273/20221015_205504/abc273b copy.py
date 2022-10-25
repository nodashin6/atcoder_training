def main():
    X, K = input().split()
    K = int(K)
    X = list(map(int, X))[::-1] + [0]*K
    print(f'{X=}')
    for i in range(K):
        a = X[i]
        if a < 5:
            X[i] = 0
        else:
            X[i] = 10
        j = 0
        while X[i+j] > 9:
            X[i+j+1] += X[i+j]//10
            X[i+j] %= 10
            j += 1
        print(f'{X=}')
    ans = ''.join(map(str, X[::-1]))
    print(int(ans))
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
