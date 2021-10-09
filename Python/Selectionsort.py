import random
from timeit import default_timer
def selectionSort(A):
    for i in range(len(A)):
      
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]

def evaluateselection(ndatos):
    A = []
    tiempo = 0.0
    for i in range(5):
        for j in range(multiplicadordatos*ndatos):
            a = random.randint(1,10000)
            A.append(a)

        inicio = default_timer()
        selectionSort(A)
        fin = default_timer()
        tiempo = tiempo + (fin-inicio)
        A.clear()

    return tiempo/5.0
