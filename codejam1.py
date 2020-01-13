

def strength(P):
   
    NEW=P.rstrip('C')
    
    length=len(NEW)
    damage=0
    i=1
    
    

    for k in range(0,length):
        if NEW[k]=='C':
            i=i*2
        if NEW[k]=='S':
            damage=damage+i
    return damage



        
def swap(D,P):
   NEW=P
   k=0
   
   if len(NEW)==NEW.count('S'):
       return -1

   while(strength(NEW)>int(D)):
       if NEW.count('S')>int(D):
           return -1
  
       
       L=list(NEW)
       length=len(L)
       L.reverse()
       
       for i in range(length-1):
           if L[i]=='S' and L[i+1]=='C':
               L[i],L[i+1]=L[i+1],L[i]
               break
       L.reverse()
       NEW="".join(L)
       
       k +=1
   return(k)




testcase=int(input())
OUTPUT=list()
for i in range(testcase):
    D,P=input().split()
                           #D____shield strength(integer)
                           #P____robot instruction(string)
            
    damage=strength(P)
    
    if(damage>int(D)):
        x=swap(D,P)
        OUTPUT.append(x)    
    else:
        x=0
        OUTPUT.append(x)

for i in range(1,testcase+1):
    if OUTPUT[i-1]==-1:
        OUTPUT[i-1]='IMPOSSIBLE'
    print('Case #'+str(i)+': '+str(OUTPUT[i-1]))
