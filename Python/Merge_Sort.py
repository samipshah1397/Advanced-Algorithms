# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:06:28 2019

@author: Samip
"""

import random 
import time
import timeit

start = time.time()


def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
  
# driver code to test the above code 
if __name__ == '__main__': 
    res = random.sample(range(1, 100001), 100000) 

#    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(res) 
    mergeSort(res) 
    print("Sorted array is: ", end="\n") 
    printList(res) 

end = time.time()
print(end - start)
#samip = timeit.timeit('"-".join(str(n) for n in range(100))', number=1)
#print(samip)
#start_time = time.time()
##main()
#print("--- %s seconds ---" % (time.time() - start_time))
