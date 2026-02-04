#Number Series:Sequential order of numbers in a particular patter
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(i)


for i in range(2,n+1,2):
    print(i)


for i in range(1,n+1,2):
    print(i)


n=int(input("Enter a number:"))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a,b=b,c

n=int(input("Enter a number:"))
for i in range(1,21):
    print(n,"x",i, "=",n*i)

for i in range(1, n+1):
    print(i**2)

for i in range(1, n+1):
    print(i**3)
