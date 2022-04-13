# union of the two list 
# li=[2,3,5,8,7]
# li1=[2,5,23,47,12]
# li2=[]
# for i in li:
#     li2.append(i)
# for i in li1:
#     li2.append(i)
# s1=set(li2)      
# s2=list(s1)
# print(s2)

#intersection 
li=[2,3,5,8,7,5,2,5]
li1=[2,5,23,47,12,2,12]
li2=[]
i=0
j=0
while(True):
    if li[i]==li1[j]:
        li2.append(li[i])
        i+=1