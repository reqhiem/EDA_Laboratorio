import random
from timeit import default_timer
def bubbleSort(arr):
    n = len(arr)
 
    for i in range(n):
 
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def evaluatebubble(ndatos):
    A = []
    tiempo = 0.0
    for i in range(5):
        for j in range(multiplicadordatos*ndatos):
            a = random.randint(1,10000)
            A.append(a)

        inicio = default_timer()
        bubbleSort(A)
        fin = default_timer()
        tiempo = tiempo + (fin-inicio)
        A.clear()

    return tiempo/5.0