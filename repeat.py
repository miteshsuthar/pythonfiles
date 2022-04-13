st=[9,4,9,6,7,4]
result=0
for i in range(len(st)):
    for j in range(len(st)):
        if i!=j and st[i]==st[j]:
            break
        j+=1
        if j==len(st):
          result=st[i]
          print(result)


         
        
