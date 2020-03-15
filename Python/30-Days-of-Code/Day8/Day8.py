#!/usr/bin/env python3

number_of_entries = int(input())
phoneBook = {}
arr = []
for i in range(0, number_of_entries):
    arr = list(map(str, input().rstrip().split()))
    phoneBook[arr[0]] = arr[1]

while True:
    try:
        query = input()
        if query in phoneBook:
            print(query + "=" + phoneBook[query])
        else:
            print("Not found")
    except:
        break
