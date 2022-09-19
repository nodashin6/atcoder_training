# ABC133D

def main():
    N = int(input())
    A = list(map(int, input().split()))
    x = 0
    for i, a in enumerate(A):
        if (N-i)%2:
            x += a
        else:
            x -= a
    B = [x]
    for a in A[:-1]:
        B.append((a-B[-1]//2)*2)
    print(*B)
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
