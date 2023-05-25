num_of_odd=0
odd_total=0
for i in range(10):
    num=int(input("enter a number: "))
    if (num%2!=0):
        odd_total+=num
        num_of_odd+=1
avg=odd_total/num_of_odd
print("sum: ",odd_total)
print("Avg: ",num_of_odd)

