def main():
    S = input()
    N = len(S)
    A = [None]*N
    dq = []
    for i in range(N):
        if S[i] == 'R':
            dq.append(i)
        elif S[i] == 'L':
            l = i
            r = i - 1
            while dq:
                j = dq.pop()
                A[j] = [l, r][(l-j)%2]
    for i in reversed(range(N)):
        if S[i] == 'L':
            dq.append(i)
        elif S[i] == 'R':
            l = i + 1
            r = i
            while dq:
                j = dq.pop()
                A[j] = [l, r][(l-j)%2]
    B = [0]*N
    for a in A:
        B[a] += 1
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
