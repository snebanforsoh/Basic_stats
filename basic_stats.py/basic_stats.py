import matplotib
x = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
count = 0
for a in x:
    count = count+1
N = count
print(N)


m = sum(x)
print(m)

mu = ((m)/N)
print(mu)


lst1 = [((a-mu)**2) for a in x]
print(lst1)

S= sum(lst1)
print(S)

C= ((S)/N-1)
print(C)

sigma= (C)**(1/2)
print(sigma)
