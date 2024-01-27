# class Person:
#     nama = "Amanda"

# obj = Person()
# print(type(obj))
# print(obj.nama)

##################################################################################################

# class Angka:
#     jumlah = 5

# a = Angka()
# print(a.jumlah)
# b = Angka()
# print(b.jumlah)

##################################################################################################

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Amanda", 20)

# print(p1.name)
# print(p1.age)

##################################################################################################

# class Person:
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score

#     def greet(self):
#         print("Hallo, " + self.name + "!")

# p1 = Person("Cecep", 20, 95)
# p2 = Person("Budi", 25, 80)

# # print(p1.name)
# # print(p1.__dict__)
# # print(p2.__dict__)

# p1.greet()
# p2.greet()

##################################################################################################

class Animal: # Parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello!")

class Cat(Animal): # child class
    def __init__(self, name, age, color, weight):
        super().__init__(name, age)
        self.color = color
        self.weight = weight

class Dog(Animal): # child class
    def __init__(self, name, age, types):
        super().__init__(name, age)
        self.type = types
