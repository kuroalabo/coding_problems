if __name__ == '__main__':
    n = int(input())
    l = list(range(n))
    for n in l:
        l[n] = n*n
    for num in l:
        print(num)
