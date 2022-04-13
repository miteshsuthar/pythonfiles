stack=[] 
def push(ch):
    stack.append(ch)
def pop():
    return stack.pop()
def peek():
    return stack[-1]
def isEmpty():
    return len(stack)==0
def priority(ch):
    if ch=='+' or ch=='-':
        return 1
    elif ch=='*' or ch=='/':
        return 2
    elif ch=='(':
        return -1
def infix_to_postfix(infix,n):
    postfix=[]
    for ch in infix:
        if ch.isalpha() or ch.isdigit():
            postfix.append(ch)
        elif ch=='(':
            push(ch)
        elif ch==')':
            while peek()!='(':
                postfix.append(pop())
            pop()
        else:
            if isEmpty()==True:
                push(ch)
            else:
                while(isEmpty()==False and priority(peek())>=priority(ch)):
                    postfix.append(pop())
                    push(ch)
        while(isEmpty()==False):
            postfix.append(pop())
        return ''.join(postfix)

infix="(a+b)*(c/d)"
postfix=infix_to_postfix(infix,len(infix))
print(postfix)