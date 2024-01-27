# List
# Append, insert
# listExample = ['Python', 42, 3.9, True, 42]

# print(listExample[0])
# print(listExample[1:4])
# print(listExample[-1])
# print(listExample)

##################################################################################################

# listExample = [42, 'Python', 3.85, 50]
# listExample.insert(1, 'Data Science')
# listExample.append("Javascript")

# print(listExample)

##################################################################################################

# remove, pop, del, clear
# listExample = [42, 'Python', 3.85, 50]
# print(listExample)

# listExample.remove('Python')
# print(listExample)

# listExample.pop()
# print(listExample)

# del listExample[2]
# print(listExample)

# listExample.clear()

##################################################################################################

# List Iteration
# listExample = [40, 55, 20, 75, 80]
# listExample2 = listExample.copy()
# listExample2[0] = 100

# print(listExample)
# print(listExample2)

# for item in listExample:
#     if item % 2 == 0:
#         print(item)

# if 40 in listExample:
#     print("Terdapat angka 40 di dalam listExample")

# listExample = [40, 55, 20]
# listExample2 = [70, 100]
# listExample.extend(listExample2)

# print(listExample + listExample2)

# listExample = [40, 55, 20]
# listExample.sort()
# listExample.reverse()
# print(listExample)
# print(listExample.index(55))
# print(listExample.sort())

##################################################################################################

# Tuple
# tupleExample = (2, 3)
# tupleExample[0] = 4

# tupleExample = ('Python', 20, 3.8, True, 20)
# print(tupleExample)
# tupleExample[1] = 30
# print(tupleExample[-2])

##################################################################################################

# Dictionary
# customer = {
#     # "id" : 100,
#     # "nama" : "Amanda",
#     # "umur" : 20

#     "nama" : "Amanda",
#     "umur" : 20
# }

# customer["nama"] = "Dambar"
# customer["pekerjaan"] = "programmer"
# customer.pop("umur")

# print(customer)
# print(customer["nama"])
# print(customer["umur"])

##################################################################################################

# Set
numbers1 = {1, 3, 5, 4, 10}
numbers2 = {3, 4, 10, 7, 8}

# {1, 3, 4, 5, 7, 8, 10}
# numbers_union = numbers1.union(numbers2) 
# print(numbers_union)

# {1, 5}
# difference1 = numbers1.difference(numbers2)
# print(difference1)

# {1, 5, 7, 8}
# sym_difference = numbers1.symmetric_difference(numbers2)
# print(sym_difference)

# {10, 3, 4}
intersect = numbers1.intersection(numbers2)
print(intersect)