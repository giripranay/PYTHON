
x,y=input().split()

s=[]

se=set()

while int(x)!=-1 and int(y)!=-1:
   # print(x,y)
    s.append(x)
    se.add(x)    
    s.append(y)
    se.add(y)
    x,y=input().split()
d={}

for i in se:
    d[i]=s.count(i)
print(d)

q=s
print(q)
q=[1 if d[t]==1 else 0 for t in s  ]
for r in range(0,l-1):
    
print(q)
l=len(s)

out=[]
i=0


    
'''
while True:
    if i>l-1:
        break
    if d[s[i]]>1:
        if d[s[i+1]]==1:
            print(0,1)
        else:
            print(-1,-1)
    else:
        if d[s[i+1]]==1:
            print(-1,-1)
        else:
            print(1,0)
    i=i+2

#print(s)

'''
