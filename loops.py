# while loop ici initialization condition increment
num = 30
while num <= 30:
    print(num)
    num += 1
# decerement
count = 5
while count >= 1:
    print("Number is :",count)
    count -= 1

# break and continue statements
x = 100
while x <= 105:
    print(x)
    if x == 103:
        break
    x += 1
y = 199
while y < 205:
     y += 1
     if y == 202:
        continue
     print(y)
# for loop
for mynum in range(5):
    print(mynum)
for num in range(80,90):
    print(num)
for z in range(1,10,3):
    print(z)
Languages = ["Python","C++","Java"]
for lang in Languages:
    print(lang)
