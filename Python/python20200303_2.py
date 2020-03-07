
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    str = input()

    count = {}
    for s in str:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

    count_sorted = sorted(count.items(), key=lambda x:x[1], reverse=True)[:3]
    for key, value in count_sorted:
        print(key, value)
#    for key in count:
#        print(key, count[key])
