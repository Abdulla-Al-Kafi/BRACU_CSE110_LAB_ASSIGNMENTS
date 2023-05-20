#1a

counter = 24

while counter>=-6:
    if counter==-6:
        print(counter)
    else:
        print(counter, end=', ')

    counter-=6

#1b

counter = -10

while counter<=20:
    if counter==20:
        print(counter)
    else:
        print(counter, end=', ')
    counter+=5

#1d
counter=18

while counter<=63:
    if counter==63:
        print(counter*-1)
    elif counter%2==0:
        print(counter, end=', ')
    else:
        print(counter*-1, end=', ')
    counter+=9