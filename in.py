n=int(input())
ar=[]
for i in range(n):
      a=input()
      ar.append(a)
ar.sort()
ar.reverse()
for i in range(len(ar)):
     if ar[i]>ar[i+1]:
          print(ar[i+1])
          break
     
     
