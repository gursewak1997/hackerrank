#!/bin/python3

# The link to the problem:
# https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&h_r=next-challenge&h_v=zen&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting

# Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.
# Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy? For example, if  and Mark has  to spend, he can buy items  for , or  for  units of currency. He would choose the first group of  items.

# Function Description
# Complete the function maximumToys in the editor below. It should return an integer representing the maximum number of toys Mark can purchase.
# maximumToys has the following parameter(s):
# prices: an array of integers representing toy prices
# k: an integer, Mark's budget

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    i = 0
    while k > 0 and i < len(prices):
        k -= prices[i]
        i += 1

    return i - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
