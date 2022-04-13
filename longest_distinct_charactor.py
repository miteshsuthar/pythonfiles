def longestSubstrDistinctChars(ar):
    for i in ar:
        if i not in st:
            st.append(i)
        else:
            break
        jn=''.join(st)
    return len(jn)
    
ar='chandrapal'
# ar='aaa'
n=len(ar)
st=[]

print(longestSubstrDistinctChars(ar))

