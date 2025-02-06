def ins(L):
    for i in range(1,len(L)):
        a=L[i]
        j=i-1
        while a<L[j] and j>=0:
            L[j+1]=L[j]
            j-=1
        L[j+1]=a
    return L


print(ins([3,4,3,4,5,7,8,53,5,6,7,9,6,5,3,4,5,6]))