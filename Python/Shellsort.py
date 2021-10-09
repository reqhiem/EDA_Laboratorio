import random
from timeit import default_timer
def shellSort(arr):

    n = len(arr)
    gap = n//2

    while gap > 0:
  
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
  
            arr[j] = temp
        gap = gap // 2

def evaluateshell(ndatos):
    A = []
    tiempo = 0.0
    for i in range(5):
        for j in range(multiplicadordatos*ndatos):
            a = random.randint(1,10000)
            A.append(a)

        inicio = default_timer()
        shellSort(A)
        fin = default_timer()
        tiempo = tiempo + (fin-inicio)
        A.clear()

    return tiempo/5.0
