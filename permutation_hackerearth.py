testcases=int(input())


def permutation(l,temp):
    print(temp)
    length=len(l)
    if l==temp:
        print("-1")
        return
    elif l==[1]*length:
        print("1")
        return
    else:
        for i in temp:
            temp[i]=temp[i]
            permutation(l,temp)
    
    


for _ in range(testcases):
    N=int(input())
    l=list(map(int,input().strip().split()))
    temp=list()
    for i in l:
        temp.append(l[i])
    permutation(l,temp)
                
