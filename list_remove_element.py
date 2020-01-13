
def lisp(element,inputlist,l):
    if inputlist==[]:
        print('nil')
        return
    inputlist.remove(element)
    f=1
    for i in range(1,len(l)):

        if f==0:
            out=inputlist.insert(i-1,l[i])
        if l[i]=="(":
            out=inputlist.insert(i-1,l[i])
            f=0
        
        if l[i]==")":
            f=1
  
    string=""
    print("("+string.join(inputlist)+")")


    
#Take input from client:

#element=input()

clientinput=input().split("'")

element=clientinput[1].strip()

l=list(clientinput[2])



inputlist=list()

f=0

for char in l[1:]:
    
    
    if char=="(":
        f=1
    
        
    if f==0 and char!=")":
        inputlist.append(char)
        
    if char==")":
        f=0
print(inputlist)
        
lisp(element,inputlist,l)




