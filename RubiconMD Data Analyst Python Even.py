# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 14:19:18 2020

@author: Rbala
ronbalaba1@gmail.com
"""




def even(start, n):
    
    integers = [] # the list we return

    # Even start
    if start % 2 == 0:  
        for i in range(start, 2*(n - 1) + start + 1): # Go through the next even integer after the start value, to the last even value
            if i % 2 == 0:
                integers.append(i)   # append only the evens
    # Odd start
    elif start % 2 != 0:  
        for i in range(start + 1, 2*(n - 1) + start + 2):  
            if i % 2 == 0:
                integers.append(i)   # append only the evens
    # Return the list at the end 
    return integers
    


    


print(even(2, 4)) # 2, 4, 6, 8
print(even(2, 5)) # 2, 4, 6, 8, 10
print(even(4, 7)) # 4, 6, 8, 10, 12, 14, 16
print(even(5, 7)) # 6 8 10 12 14 16 18
print(even(100, 1))  # 100
print(even(28, 3))  # 28, 30, 32
print(even(5, 3))  # 6,8,10
print(even(7, 2))  # 8, 10
print(even(11,4))  # 12,14,16,18
print(even(79,5))  # 80, 82, 84, 86, 88
print(even(143, 3))  # 144, 146, 148
print(even(179,4))  # 180, 182, 184, 186
print(even(5,12) == even(6,12))  # True
print()






