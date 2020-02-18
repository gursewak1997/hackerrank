#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(alist):
    count = 0
    for i in range(len(alist)-1,0,-1):
       for j in range(i):
           if alist[j] > alist[j+1]:
               temp = alist[j]
               alist[j] = alist[j+1]
               alist[j+1] = temp
               count = count+1
    print("Array is sorted in "+str(count)+" swaps.")
    print("First Element: "+str(alist[0]))
    print("Last Element: "+str(alist[len(alist)-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
