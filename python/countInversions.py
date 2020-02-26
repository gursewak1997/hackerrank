#!/bin/python3
#Link to the problem:
#https://www.hackerrank.com/challenges/ctci-merge-sort/problem
import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def sort(arr):
    a, ind = countInversions(arr)
    return ind

def countInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:int(len(arr)/2)]
        b = arr[int(len(arr)/2):]
        a, ai = countInversions(a)
        b, bi = countInversions(b)
        c = []
        i = 0
        j = 0
        inversions = 0 + ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a)-i)
    c += a[i:]
    c += b[j:]
    return c, inversions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = sort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
