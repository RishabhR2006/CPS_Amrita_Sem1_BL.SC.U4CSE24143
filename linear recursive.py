i=0
pos=-1
def search(L,n,i):
    globals()['i']
    if L[i]==n:
        globals()['pos']=i
        return True
    i+=1
    search(L,n,i)
    if i==len(L):
        return False


L=[1,2,3,4,5,6,7,8,9]
n=6

if search(n,L,i):
    print("number found at ",pos+1)
else:
    print("not found")