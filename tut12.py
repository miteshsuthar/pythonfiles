st=[-1,2,-1,3,2]
x=0
st.sort()
print(st)
for i in range(0,len(st)):
    if st[i]==st[i+1]:
        i+=1
    else:
        x=st[i+1]
        break
print(x)