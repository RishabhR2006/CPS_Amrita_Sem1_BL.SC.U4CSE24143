def bubblesort(l):
    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)-1):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    print (l)

def selectionsort(l):
    for i in range(0,len(l)):
        min = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min]:
                min = j
        l[i], l[min] = l[min], l[i]

    print (l)

def insertionsort(l):
    for i in range(1, len(l)):
        x = l[i]
        j = i - 1
        while j >= 0 and x < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = x

    print (l)

l=[2,1,4,6,3,5]
bubblesort(l)
selectionsort(l)
insertionsort(l)
