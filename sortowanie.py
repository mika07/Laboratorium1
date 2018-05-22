import numpy as np
import time as t

alist1 = np.arange(5000)
np.random.shuffle(alist1)

alist=np.arange(5000)
np.random.shuffle(alist)

alist2 = np.arange(5000)
np.random.shuffle(alist2)

print(alist1)
l = len(alist1)
czas_pocz=t.time()
for a in range(l):
    for b in range(l-1):
        if (alist1[a] < alist1[b]):
            alist1[a], alist1[b] = alist1[b], alist1[a]

print(alist1)
czas_koniec=t.time()
wynik=czas_koniec-czas_pocz
print("Bubble sort:"+str(wynik))

print(alist)
czas_pocz=t.time()
for i in range(len(alist)):
    minimum = i
    for k in range(i + 1, len(alist)):
        if alist[k] < alist[minimum]:
            minimum = k
    tmp=alist[minimum]
    alist[minimum]=alist[i]
    alist[i]=tmp

print(alist)
czas_koniec=t.time()
wynik=czas_koniec-czas_pocz
print("Selection sort:"+str(wynik))

czas_pocz=t.time()
def sort(array):
    lewa_strona = []
    piwot = []
    prawa_strona = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                lewa_strona.append(x)
            if x == pivot:
                piwot.append(x)
            if x > pivot:
                prawa_strona.append(x)
        return sort(lewa_strona)+ piwot +sort(prawa_strona)
    else:
        return array



print(sort(alist2))
czas_koniec=t.time()
wynik=czas_koniec-czas_pocz
print("Quick Sort:"+str(wynik))