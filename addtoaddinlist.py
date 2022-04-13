l=[143,15,27,3654]
li=[]
for i in l:
    count =0
    str_ele=str(i)
    for j in str_ele:
        count = count+int(j)
    li.append(count)
print(li)