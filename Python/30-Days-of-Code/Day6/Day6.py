number_of_test_case = int(input())

# 初期化
print_string = []

# 受け取って加工
for i in range(0, number_of_test_case):
    given_string = input()
    length_string = len(given_string)
    odd_string = str()
    even_string = str()
    for j in range(0, length_string):
        if j % 2 == 0:
            odd_string = odd_string + given_string[j]
        else:
            even_string = even_string + given_string[j]
    #print_string.append(odd_string + " " + even_string)
    print_string[i] = odd_string + " " + even_string


for x in range(0, len(print_string)):
    print(print_string[x])
