

def poss(n):
    brace=[]
    print("dsgs")
    possout=formation(n,brace)
    
        
def formation(n,brace):
    if n==len(brace):
        print(brace)
        return
    formation(n,brace.append("("))
    
    
    
    
x=input()

poss(x)
