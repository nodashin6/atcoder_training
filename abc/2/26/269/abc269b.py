# ABC269B

def main():
    S = [input() for _ in range(10)]
    hi = []
    we = set([])
    for h in range(10):
        if '#' in S[h]:
            hi.append(h)
            for w in range(10):
                if S[h][w] == '#':
                    we.add(w)

    print(min(hi)+1, max(hi)+1)
    print(min(we)+1, max(we)+1)

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
