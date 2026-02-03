'''
Docstring for ListComprehensive
List Comprehensions
List Comprehension giup ban viet code ngan gon (dac biet khi dang o trong 1 vong lap da co)
va de doc, nhin code hon
'''

# new_list[<action> for <item> in <iterator> if <some condition>]

word = "Hello World"

#Option1
for char in word:
    print(char)

#Option2

print([char for char in word])


#
even_numbers = [i for i in range(0,10) if i % 2 ==0]

print(even_numbers)

#
transactions = [ 100, 200, 300, 150, 80]
tax_rate = 0.08
service_charge = 0.07

def get_price_tax_service(bill):
    return bill * (1 + tax_rate + service_charge)

print(get_price_tax_service(100))

final_prices = [ get_price_tax_service(bill) for bill in transactions]
print(final_prices)

# Advanced Functions

#list() --> convert strings ==> List
my_strings = "Welcome to DataXplore Channel"
list_of_chars = list(my_strings)
print(list_of_chars)
print(list(my_strings))

#sum
print(sum([1,2,3,4,5]))

#zip(): looping through 2 list simultaneously
wizards = ['Harry Potter', 'Ron', 'Hermione']
pets = ['Hedwig', 'Scabber', 'Crookshank']

for wiz, pet in zip(wizards, pets):
    print(f'{wiz} has {pet}')


for index, (wiz, pet) in enumerate(zip(wizards, pets), start = 1):
    print(f"{index}. {wiz} has {pet}")

#sorted
sorted_by_first = sorted(['hi', 'hello','you', 'DataXplore'], key = lambda el: el[1])
print(sorted_by_first)


sorted_by_key = sorted([{'name': 'DatXplore', 'age': 15},{'name': 'Andy', 'age': 18},{'name': 'Zoey', 'age': 25}], key = lambda el: el['name'])
print(sorted_by_key)

# 2D Array/List = Matrix: Mang 2 chieu

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix[1][2])

for row in range(len(matrix)):
    for col in range(len(matrix)):
        print(matrix[row][col])

#transform matrix in list
list_converted = [matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix))]
print(list_converted)

#combine columns with zip and *:
print([x for x in zip(*matrix)])