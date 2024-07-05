# A class is a blueprint of an object
# Object is an instance of a class
#a class should have 2 parts
class Person:
    #properties/attribute/variable/characteristics
    name = "Morris"
    age = 21
    gender ="Male"

    #behaviour/method/function
    def walk(self):
        print("Person is walking")

person1 = Person()
print(person1.gender)
print(person1.name)
print(person1.age)
person1.walk()