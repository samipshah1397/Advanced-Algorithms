# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:10:22 2019

@author: Samip
"""

# Python program for implementation of Insertion Sort 
import random
import time


start = time.time()

# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
  
# Driver code to test above 
#arr = [12, 11, 13, 5, 6] 
res = random.sample(range(1, 100000), 25000) 
print ("Given array is", end="\n")  
print(res) 
insertionSort(res) 
print ("Sorted array is:") 
print(res)

end = time.time()
print(end - start)
  
