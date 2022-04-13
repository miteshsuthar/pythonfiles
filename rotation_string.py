s1='ABCD'
# s2="BCDA"
s2='ACBD'
s3=s1*2
if len(s1)==len(s2):
    if s2 in s3:
        print(True) 
    else:
        print(False)
