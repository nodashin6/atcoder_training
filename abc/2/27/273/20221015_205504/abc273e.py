from collections import defaultdict
def main():
    Q = int(input())
    a = [-1]
    c = [0]
    saved = defaultdict(int)
    for q in range(1, Q+1):
        s, x = query_input()
        if s == 'ADD':
            c.append(q-1)
            a.append(x)
            
        elif s == 'DELETE':
            a.append(a[c[-1]])
            c.append(c[c[q-1]])
            

        elif s == 'SAVE':
            c.append(c[-1])
            a.append(a[-1])
            saved[x] = q

        elif s == 'LOAD':
            c.append(c[saved[x]])
            a.append(a[saved[x]])
            
    print(*a[1:])

    # print(f'{a=}')
    # print(f'{c=}')
    return 

def query_input():
    l = input()
    if ' ' in l:
        s, x = l.split()
        x = int(x)
    else:
        s = l
        x = None
    return s, x

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
