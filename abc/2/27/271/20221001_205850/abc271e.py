def main():
    INF = 1<<62
    N, M, K = map(int, input().split())
    G = []
    for _ in range(M):
        u, v, c = map(int, input().split())
        G.append([u-1, v-1, c])


    E = [x-1 for x in map(int, input().split())]
    C = [INF] * N
    C[0] = 0
    for e in E:
        u, v, c = G[e]
        C[v] = min(C[v], C[u]+c)
    
    ans = C[-1]
    if ans == INF:
        ans = -1
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
