n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    if i%7==0:
        sum=sum+i

print(sum)