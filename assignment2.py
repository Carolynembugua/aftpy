# write a prog that prompts the user to:
#enter a number and checks whether it is prime or not
# a prog that allows you to enter an alphabet and return it as either a vowel or a consonant



#1
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2,int (num/2)+1):
        if (num % i) == 0:
            print(num,"number is not prime")
        break

    else:
        print(num,"number is prime")
else:
    print(num,"number is  not prime")

#2
x = str(input("Enter an alphabet :"))
if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U'):
    print(x,"is a vowel")
else:
    print(x,"is a consonant")

#3
class Books:
    def fiction(self):
        print("This is a fiction book")
class Write(Books):
    def anime(self):
        print("This is a anime book")
class Read(Write):
    def thriller(self):
        print("This is a thriller book")

b = Books()
w = Write()
r = Read()
