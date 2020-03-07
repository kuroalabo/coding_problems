# import pdb; pdb.set_trace()

for n in range(2, 10):
    print(n) 
    for x in range(2, n):
        print(x)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
