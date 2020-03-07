if __name__ == '__main__':
    n = int(input())
    r = range(1,n+1)
    result = ""
    for element in r:
        result = str(result) + str(element)
    print(result)
