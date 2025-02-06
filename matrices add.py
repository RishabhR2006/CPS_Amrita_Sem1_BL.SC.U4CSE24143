x=[[1,2,3],[2,3,4],[3,4,5]]
y=[[3,2,1],[4,3,2],[5,4,3]]

rest=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        res[i][j]=x[i][j]+y[i][j]
for r in res:
print(r)
