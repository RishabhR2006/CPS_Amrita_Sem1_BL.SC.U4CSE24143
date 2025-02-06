# a=int(input("enter a number"))
# x=[[1,2,3],[2,3,4],[3,4,5]]
# result=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j]=x[i][j]*a
# for r in result:
#     print(r)

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
a=int(input("enter a number"))
result=[]
for i in range(len(x)):
    bro=[]
    for j in range(len(x[0])):
        le=x[i][j]*a
        bro.append(le)
    result.append(bro)
    
print("resultant matrix:")
for r in result:
    print(r)