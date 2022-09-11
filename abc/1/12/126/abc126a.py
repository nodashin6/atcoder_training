# ABC126A

def main():
    N, K = map(int, input().split())
    S = list(input())
    S[K-1] = S[K-1].lower()
    print(''.join(S))


if __name__ == '__main__':
    try:
        f = open('./input.txt')
        input = lambda: f.readline().rstrip()
    except:
        pass
    main()