# -*- coding: utf-8 -*-


import random 
import time

st = time.time()


def mergeSort(array): 
    if len(array) >1: 
        mid = len(array)//2 #Finding the mid of the array 
        L = array[:mid] # Dividing the array elements  
        R = array[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                array[k] = L[i] 
                i+=1
            else: 
                array[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            array[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            array[k] = R[j] 
            j+=1
            k+=1
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
  
# driver code to test the above code 
if __name__ == '__main__': 
    re = random.sample(range(1, 10000), 8000) 

#    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(re) 
    mergeSort(re) 
    print("Sorted array is: ", end="\n") 
    printList(re) 

end = time.time()
print(end - st)
#samip = timeit.timeit('"-".join(str(n) for n in range(100))', number=1)
#print(samip)
#start_time = time.time()
##main()
#print("--- %s seconds ---" % (time.time() - start_time))
