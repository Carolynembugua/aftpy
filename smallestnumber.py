first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))
fourth = int(input("Enter fourth number: "))
if first < second and first < third and first < fourth:
    print("The smallest number is", first)
elif second < third and second < fourth and second < first:
    print("The smallest number is", second)
elif third < fourth and third < first and third < second:
    print("The smallest number is", third)
else:
    print("The smallest number is", fourth)
