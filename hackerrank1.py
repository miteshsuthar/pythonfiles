n=int(input())
l= list(map(int,input().strip().split()))[:n]
l.sort(reverse=True)
for j in range(len(l)):
    print(l[j])
    break
