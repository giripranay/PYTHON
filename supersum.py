

def Supersum(num):
    if len(num)==1:
        print(num)
        return

    
    s=0;
    for x in num:
        s=s+int(x)
    
    newsupersum=str(s)
    Supersum(newsupersum)
   


num=str(input())

Supersum(num)
