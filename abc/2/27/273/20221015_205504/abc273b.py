def main():
    X, K = map(int, input().split())
    x = X
    for i in range(K):
        k = 10**(i+1)
        a = x%k
        a = int(str(a)[0])
        if a < 5:
            x = x//k 
            x *= k
        else:
            x = (1 + x//k)*k
    print(x)

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
