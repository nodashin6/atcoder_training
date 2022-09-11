# ABC126B

def main():
    ANS = ['YYMM', 'MMYY', 'AMBIGUOUS', 'NA']
    S = input()
    x = int(S[:2])
    y = int(S[2:])
    if 0< x < 13 and 0< y < 13:
        print(ANS[2])
    elif 0< y < 13:
        print(ANS[0])
    elif 0< x < 13:
        print(ANS[1])
    else:
        print(ANS[3])


if __name__ == '__main__':
    try:
        f = open('./input.txt')
        input = lambda: f.readline().rstrip()
    except:
        pass
    main()