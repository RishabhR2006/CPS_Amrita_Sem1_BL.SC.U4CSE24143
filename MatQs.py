"""Sort a list of lists (matrix) by the sum of each inner list, and then
search for a specific sum in the sorted matrix."""

def Sum_Sort(arr,size):
    for i in range(size):
        _min=i
        for j in range(i+1,size):
            if sum(arr[j])<sum(arr[_min]):
                _min=j
        arr[i],arr[_min]=arr[_min],arr[i]

def Sum_Search(arr,x,size):
    for i in range(size):
        if sum(arr[i])==x:
            return i
    else:
        return -1


l=[[10,9,8],[5,6,7],[1,2,3],[4,3,1]]
Sum_Sort(l,len(l))
print("Sorted List: ",l)
S_Sum=int(input("Enter the sum to be searched: "))
x=Sum_Search(l,S_Sum,len(l))
if x==-1:
    print("Sum Not Found in list")
else:
    print("Sum found,Element:",l[x],"at position",x+1)
