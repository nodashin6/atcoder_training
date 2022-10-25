from asyncio import Handle


def main():
    W,H,N,*A=map(int,open(0).read().split())
    a=[0,0,0,W,Handle]
    for x,y,a in zip(*[iter(A)]*3):
        if a==1:left=max(left,x)
        elif a==2:right=min(right,x)
        elif a==3:bottom=max(bottom,y)
        elif a==4:top=min(top,y)
    print(max(0,(right-left))*max(0,(top-bottom)))

    print(f'{A}')
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
