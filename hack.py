from itertools import permutations
x=input()
y=input()
z=input()
perm = permutations([x,y,z])
for i in list([perm]):
    print ([i],end='')