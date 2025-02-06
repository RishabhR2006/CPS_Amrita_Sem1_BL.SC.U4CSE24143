def sel(L):
    for i in range(len(L)):
        min=i
        for j in range(i+1,len(L)):
            if L[j] < L[min]:
                min = j
        if min != i:
            L[i],L[min]=L[min],L[i]
    return L


print(sel([3,4,3,4,5,7,8,53,5,6,7,9,6,5,3,4,5,6]))