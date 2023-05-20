#using while loop
counter=10
while counter<=50:
    if counter%2!=0:
        print(counter, end=' ')
    counter+=1

#using for loop
print("\n==========Using For Loop==========")
for i in range(10,50):
    if i%2!=0:
        print(i, end=' ')
