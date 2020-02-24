#!/bin/python3
#https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&h_r%5B%5D%5B%5D=next-challen#ge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=z#en&isFullScreen=false&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D=interview-preparatio#n-kit&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D=sorting

import os
from bisect import bisect_left, insort_left



# Complete the activityNotifications function below.
def activityNotifications(t, d):
    result = 0;
    sliced = sorted(t[:d])
    for i in range(d,len(t)):
        if t[i] >= 2*median(sliced): result += 1
        del sliced[bisect_left(sliced, t[i-d])]
        insort_left(sliced, t[i])
    return result;
    
def median(sliced):
    return sliced[d//2] if d%2 == 1 else ((sliced[d//2] + sliced[d//2-1])/2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
