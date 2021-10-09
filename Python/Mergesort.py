import random
from timeit import default_timer
def mergeSort(arr):
    if len(arr) > 1:
  
        mid = len(arr)//2
  
        L = arr[:mid]
  
        R = arr[mid:]
  
        mergeSort(L)
  
        mergeSort(R)
  
        i = j = k = 0
  
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def evaluatemerge(ndatos):
    A = []
    tiempo = 0.0
    for i in range(5):
        for j in range(multiplicadordatos*ndatos):
            a = random.randint(1,10000)
            A.append(a)

        inicio = default_timer()
        mergeSort(A)
        fin = default_timer()
        tiempo = tiempo + (fin-inicio)
        A.clear()

    return tiempo/5.0
