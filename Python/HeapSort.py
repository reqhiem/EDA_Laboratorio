import random
from timeit import default_timer
def heapify(arr, n, i):
    largest = i 
    l = 2 * i + 1    
    r = 2 * i + 2     
 
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
 
        heapify(arr, n, largest)
 
def heapSort(arr):
    n = len(arr)
 
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)
        
def evaluateheap(ndatos):
    A = []
    tiempo = 0.0
    for i in range(5):
        for j in range(multiplicadordatos*ndatos):
            a = random.randint(1,10000)
            A.append(a)

        inicio = default_timer()
        heapSort(A)
        fin = default_timer()
        tiempo = tiempo + (fin-inicio)
        A.clear()

    return tiempo/5.0
