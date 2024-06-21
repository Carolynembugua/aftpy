temperature = 34
if temperature > 25:
    print("it is too hot")
elif temperature < 25:
    print("it is cold")
else:
    print("normal temperature")

#a programme that returns the largest number among new numbers
first = 78
second = 34
third = 100

if first > second and first > third:
    print(first,"is the largest")
elif second > first and second > third:
    print(second,"is the largest")
else:
    print(third,"is the largest")

#programme that checks whether a number is even or odd

for numbers in range(0,20):
    if(numbers % 2 == 0 ) :
        print(numbers)
    elif (numbers % 2 == 1):
        print(numbers)
