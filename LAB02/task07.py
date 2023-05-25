num1=int(input("enter a number: "))
sum1=0
sum2=0
count=0

while count<=num1:
    if count%2==0:
        sum1=sum1-(count**2)
    else:
        sum2=sum2+(count**2)

    count+=1

total_sum1=sum1+sum2
print(total_sum1)

#=====using while loop=====
num2=int(input("enter a number: "))
sum3=0
sum4=0

for i in range(1,num2+1):
    if i%2==0:
        sum3=sum3-(i**2)
    else:
        sum4=sum4+(i**2)

total_sum2=sum3+sum4
print(total_sum2)
