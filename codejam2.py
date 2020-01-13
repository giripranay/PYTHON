def TroubleSort(L):
    flag=0
    n=len(L)
    while flag==0:
        flag=1
        for i in range(0,n-2):
            if L[i]>L[i+2]:
                flag=0
                L[i],L[i+2]=L[i+2],L[i]

    for i in range(n-1):
        if L[i+1]<L[i]:
            return i
    return 'OK'        



testcase=int(input())
OUTPUT=list()
for i in range(testcase):
    n=int(input())
    L=input().split()
    for i in range(n):
        L[i]=int(L[i])
    x=TroubleSort(L)
    OUTPUT.append(x)
for i in range(1,testcase+1):
    print('Case #'+str(i)+': '+str(OUTPUT[i-1]))
