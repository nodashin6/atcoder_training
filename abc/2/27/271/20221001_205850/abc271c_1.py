from collections import deque
def main():
    INF = 1<<62
    N = int(input())
    A = list(map(int, input().split()))

    dq = deque(sorted(set(A)))
    for _ in range(N-len(dq)):
        dq.append(INF)

    read = [0]
    while dq:
        a = dq.popleft()
        if a == read[-1] + 1:
            read.append(a)
        elif a > read[-1] + 1:
            dq.appendleft(a)
            if len(dq) > 1:
                dq.pop()
                dq.pop()
                read.append(read[-1] + 1)
            else:
                break
    ans = len(read) - 1
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
