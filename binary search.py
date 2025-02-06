pos=-1
def search(l,u,L,n):
    while l<=u:
        mid=(l+u)//2
        if L[mid]==n:
            globals()['pos']=mid+1
            return True
        elif L[mid]<n:
            l=mid+1
        elif L[mid]>n:
            u=mid-1
    return False

L=[3,5,7,9,56,345,899,5069]
n=8999

if search(0,len(L)-1,L,n):
    print("element found at position ",pos)
else:
    print("element not found")