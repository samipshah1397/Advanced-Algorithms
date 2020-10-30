# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:44:04 2019

@author: Samip
"""

def partition(array,p,r): 
    i = ( p-1 )         # index of smaller element 
    part_indexvot = array[r]     # part_indexvot 
  
    for j in range(p , r): 
  
        # If current element is smaller than or 
        # equal to part_indexvot 
        if   array[j] <= part_indexvot: 
          
            # increment index of smaller element 
            i = i+1 
            array[i],array[j] = array[j],array[i] 
  
    array[i+1],array[r] = array[r],array[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# array[] --> arrayay to be sorted, 
# p  --> Starting index, 
# r  --> Ending index 
  
# Function to do Quick sort 
def quickSort(array,p,r): 
    while p < r: 
  
        # part_index is partitioning index, array[p] is now 
        # at right place 
        part_index = partition(array,p,r) 
        
#        samip = part_index - p
#        shah = r-part_index
        
        if part_index - p < r-part_index:
            quickSort(array,p,part_index-1)
            p = part_index+1
        else:
            quickSort(array, part_index + 1, r)
            r = part_index - 1
        # Separately sort elements before 
        # partition and after partition 
#        quickSort(array, p, part_index-1) 
#        #quickSort(array, part_index+1, r)
#        p = part_index+1 
  
# Driver code to test above 
array = [5, 6, 8, 10, 11, 13, 8, 8, 3, 5, 2, 11, 8] 
n = len(array) 
quickSort(array,0,n-1) 
print ("Sorted arrayay is:") 
for i in range(n): 
    print ("%d" %array[i]),