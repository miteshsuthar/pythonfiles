# All digits are different  then return True and same digits then return False
 
def fun(N):
    st=str(N)
    for i in range(len(st)):
        for j in range(len(st)):
            if i!=j and st[i]==st[j]:
                return False 
    return True             
    
N=int(input())
print(fun(N))    
    


    

          

            

