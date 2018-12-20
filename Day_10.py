#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    a = str(bin(n)[2:])        
    # print(a)


    b = a.split("0")
    # print(b)
    max_length = 0
    for i in b:
        if len(i) > max_length:
            max_length = len(i)
        
    print (max_length)

