# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:10:22 2019

@author: Samip
"""

# Python program for implementation of Insertion Sort 
import random
import time


st = time.time()

# Function to do insertion sort 
def insertionSort(array): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(array)): 
  
        key = array[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < array[j] : 
                array[j+1] = array[j] 
                j -= 1
        array[j+1] = key 
  
  
# Driver code to test above 
#arr = [12, 11, 13, 5, 6] 
re = random.sample(range(1, 10000), 8000) 
print ("Given array is", end="\n")  
print(re) 
insertionSort(re) 
print ("Sorted array is:") 
print(re)

end = time.time()
print(end - st)
  
