# ABC131A

def main():
    S = input()
    ans = 'Good'
    for si, sj in zip(S[:-1], S[1:]):
        if si == sj:
            ans = 'Bad'
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
