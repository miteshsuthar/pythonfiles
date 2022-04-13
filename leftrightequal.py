def left_right(ar,n):  
    ls=ar[0]   
    rs=0
    flag=1
    for i in range(1,n):
        rs=rs+ar[i]
    for i in range(1,n):
        rs=rs-ar[i]
        if ls==rs:
            print(ar[i])
            flag=0
            break
        else:
            ls=ls+ar[i]
    if flag==1:
        print("element not found ")   
ar=[2,3,4,1,4,5]
n=len(ar)
left_right(ar,n)