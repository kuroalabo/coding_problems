N = input()
L = list(map(int, input().strip().split()))
count = 0
while all(elements % 2 == 0 for elements in L ):
    L = [elements/2 for elements in L]
    count += 1
print(count)
