i=0
j=0
string='ThIsisCoNfUsInG'
sub_string='is'
count=0
n=len(sub_string)
n1=len(string)
while i<n1-1:
    if string[i]!= sub_string[j]:
        i+=1
    else:
        i+=1
        j+=1
        if(n-1)==j:
            count+=1  
            j=0   
       
print(count)