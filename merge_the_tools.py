def merge_the_tools(string,k):
    # your code goes here
    n=len(string)
    s=set()
    arr=' '
    for i in range(n):
        if len(arr)!=k:
            arr=arr+(string[i])
            print(arr)
        if len(arr)==k:
            s.add(arr)
            print(s)
    return 0
string, k = input(), int(input())

merge_the_tools(string, k)