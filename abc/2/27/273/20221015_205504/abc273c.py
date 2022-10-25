import bisect
from functools import lru_cache

def main():
    global B
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(set(A))
    ans = [0]*N
    for a in A:
        k = count_greater(a)
        ans[k] += 1
    print(*ans, sep='\n')
    return

@lru_cache(maxsize=None)
def count_greater(a):
    i = bisect.bisect_left(B, a)
    return len(B)-i-1

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
