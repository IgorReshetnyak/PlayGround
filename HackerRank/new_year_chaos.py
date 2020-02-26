#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    b=0
    i=len(q)-1
    while i>=0:
        di=q[i]-i-1
        print(di,file=sys.stderr)
        if di>0:
            if di>2: b="Too chaotic"; break
            elif di==1: q[i]=q[i+1];q[i+1]=i; b+=1; i+=1
            else: q[i]=q[i+1]; q[i+1]=q[i+2]; q[i+2]=i+1; b+=2; i+=2
        i-=1
    
    print(b)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
