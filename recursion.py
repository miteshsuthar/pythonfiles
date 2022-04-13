def reverse(n, s):
    if n > 0:
        s = s*10 + n%10
        reverse(n//10, s)
    else:
        print(s)
n = int(input("Enter number"))
d = reverse(n, 0)