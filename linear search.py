pos=-1
def search(L,n):
    for i in range(len(L)):
        if L[i]==n:
            globals()['pos']=i+1
            return True
    return False
    
L=[1,2,5,7,8,3,4]
n=9

if search(L,n):
    print("element found at position ",pos)
else:
    print("element not found")