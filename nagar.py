arr=['tarks','arkSt','kStar','trs','tSk']
arr1=arr.copy()
string='Stark'
string1=string.lower()
print(string1)
l=[]
l1=[]
def rotate(input,d):
   Rfirst = input[0 : len(input)-d]
   Rsecond = input[len(input)-d : ]
   l.append(Rsecond + Rfirst)
d=1
for i in range(len(string)):
    rotate(string,d)
    d+=1
d=0
for i in range(len(string1)):
    rotate(string1,d)
    d+=1

for x in range(len(arr)):
    if arr[x] in l:
        l1.append(arr[x])
        arr1.remove(arr[x])

print(','.join(l1))
print(arr1)