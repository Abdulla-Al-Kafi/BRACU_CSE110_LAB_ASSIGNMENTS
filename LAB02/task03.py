# using while loop
counter=0
sum=0
while counter<=600:
    if counter%7==0 and counter%9==0:
        sum=sum+counter
    counter+=1
print(sum)

#using for loop
sum=0
for i in range(0,601):
    if i%7==0 and i%9==0:
        sum=sum+i
print(sum)