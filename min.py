l=[10,20,30,5,8,10.3]
min=l[0]
max=l[0]
for i in l[1: ]:
    if i<min:
        min=i
    if i>max:
        max=i
print(min)
print(max)