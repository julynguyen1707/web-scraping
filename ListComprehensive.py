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