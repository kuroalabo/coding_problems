if __name__ == '__main__':
    n = int(input())
    l = list(range(1, n+1))
    result = map(strip(), l)
    print(list(result))
