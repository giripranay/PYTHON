





x=int(input())
y=int(input())

Matrix=list()

for i in range(x):
    newlist=list()
    for j in range(y):
        newlist.append(int(input()))
    Matrix.append(newlist)
N=int(input())

def clearneighbour(a,b):
    Matrix[a][b]=-1
    if a-1>0 and b-1>0:
        Matrix[a-1][b-1]=-1
        Matrix[a-1][b]=-1
        Matrix[a][b-1]=-1
    if a-1>0 and b-1<0:
        Matrix[a-1][b]=-1
    if a-1<0 and b-1>0:
        Matrix[a][b-1]=-1
    if a+1<x and b+1<y:
        Matrix[a+1][b+1]=-1
        Matrix[a+1][b]=-1
        Matrix[a][b+1]=-1
    if a+1<x and b+1>y-1:
        Matrix[a+1][b]=-1
    if a+1>x-1 and b+1<y:
        Matrix[a][b+1]=-1
    if a-1>0 and b+1<y-1:
        Matrix[a-1][b+1]=-1
    if a+1<x-1 and b-1>0:
        Matrix[a+1][b-1]=-1



for i in range(N):
    for j in range(x):
        for k in range(y):
            if Matrix[j][k]==-1:
                Matrix[j][k]=i+1
    for j in range(x):
        for k in range(y):
            if Matrix[j][k]==i:
                clearneighbour(j,k)
                
print(Matrix)    

