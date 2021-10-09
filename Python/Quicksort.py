import random
from timeit import default_timer

def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]     
    for j in range(low, high):
        if arr[j] <= pivot:
  
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
  
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        pi = partition(arr, low, high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def evaluatequick(ndatos):
    A = []
    tiempo = 0.0
    for i in range(5):
        for j in range(multiplicadordatos*ndatos):
            a = random.randint(1,10000)
            A.append(a)

        inicio = default_timer()
        quickSort(A,0,multiplicadordatos*ndatos-1)
        fin = default_timer()
        tiempo = tiempo + (fin-inicio)
        A.clear()

    return tiempo/5.0
