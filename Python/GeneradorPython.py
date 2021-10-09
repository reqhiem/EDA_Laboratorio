import random
import sys
from timeit import default_timer
from matplotlib import pyplot as plt

multiplicadordatos = 1000
#archivo = open('archivo.txt','r');
#print (archivo.read());
#archivo.close
timesbubble = []
timesheap = []
timesinsertion = []
timesselection = []
timesshell = []
timesmerge = []
timesquick = []
for i in range(1,11):
    time = evaluatebubble(i)
    timesbubble.append(time)
print("Bubble terminado")
for i in range(1,11):
    time = evaluateheap(i)
    timesheap.append(time)
print("Heap terminado")
for i in range(1,11):
    time = evaluateinsertion(i)
    timesinsertion.append(time)
print("Insertion terminado")
for i in range(1,11):
    time = evaluateselection(i)
    timesselection.append(time)
print("Selection terminado")
for i in range(1,11):
    time = evaluateshell(i)
    timesshell.append(time)
print("Shell terminado")
for i in range(1,11):
    time = evaluatemerge(i)
    timesmerge.append(time)
print("Merge terminado")
for i in range(1,11):
    time = evaluatequick(i)
    timesquick.append(time)
print("Quick terminado")

datos = [100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000]
plt.plot(datos,timesbubble,datos,timesheap,datos,timesinsertion,datos,timesselection,datos,timesshell,datos,timesmerge,datos,timesquick)
plt.legend(['Bubblesort','Heapsort','Insertionsort','Selectionsort','Shellsort','Mergesort','Quicksort'],loc=2)
plt.show()

