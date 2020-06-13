# Quick Sort


def quick_part(array,low,high):  # a denotes to array , low denotes as index of smaller element and high as larger element
    i = ( low-1 )         
    pivot = array[high]     # to store highest value
  
    for j in range(low,high): 
        if   array[j] <= pivot: 
            i = i+1 
            array[i],array[j] = array[j],array[i] 
  
    array[i+1],array[high] = array[high],array[i+1] 
    return ( i+1 ) 
  



# Function 
def quickSort(array,low,high): 
    if low < high: 
        pi = quick_part(array,low,high) 
  
        quickSort(array, low, pi-1) 
        quickSort(array, pi+1, high) 
  


array = [8,5,7,3,6,2,4,9,1,0,9,5,9] 
n = len(array) 

print("The Original Array before sorting is:")
for i in range(n):
  print("%d" %array[i], end =',')
quickSort(array,0,n-1) 
print ("\n\nSorted array using Quick Sort Algorithm is:") 
for i in range(n): 
    print ("%d" %array[i], end =',')




# Merge Sort


import math    

def merge_sort(array, lower, higher):
    
    if lower < higher:
        # dividing mid value
        m = (lower + higher) // 2

        merge_sort(array, lower, m)

        merge_sort(array, m + 1, higher)

        merge(array, lower,m , higher)


def merge(array, lower,  m , higher):
   
    nL = m - lower + 1

   
    nH =higher - m

    L = [0] * (nL + 1)
    H = [0] * (nH + 1)

  
    for i in range(0, nL):
        L[i] = array[lower + i]


    for j in range(0, nH):
        H[j] = array[m + 1 + j]

  
    L[nL] = math.inf
    H[nH] = math.inf

    i = 0
    j = 0
    for k in range(lower, higher + 1):
        if L[i] <= H[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = H[j]
            j += 1






A = [9,5,2,3,8,5,3,6,4,1]
print("Original Array:",A)
merge_sort(A, 0, len(A) - 1)

print("Sorted Array using Merge Sort:",A)
    