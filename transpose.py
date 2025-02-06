b=int(input("enter no of rows"))
c=int(input("enter no of columns"))
x=[]
for i in range(b):
    row=[]
    for j in range(c):
        ele=int(input())
        row.append(ele) 
    x.append(row)
print("your matrix:")
for r in x:
     print(r)   
print("transposed matrix:")
for j in range(len(x[0])):
    for i in range(len(x)):
        