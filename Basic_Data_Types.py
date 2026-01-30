# Basic data types in python: bool, none, int, float, str
'''
Docstring for Basic_Data_Types
'''

'''
Topic #0: bool & None
'''
# [] bool: True & False
# True = 1 
# False = 0
var_bool = True

# [] type(): Dynamically typed
print(type(var_bool))

# Numerically, they're evaluated as integers with value 1(True), 0(False)
a = 4 + True
print(a)

b = False
if b==0:
    print("B is zero")

# None: Phan tu khong
var_none = None

print(type(var_none))

# None is often used as a placeholder for optional or missing value
# It evaluates as False in conditionals.
# email_address = None
email_address = "trannguyen.analytics@gmail.com"
if email_address:
    print(f"Email address is {email_address}")
else:
    print(f"Email address is empty")


# [] Number: int (Integer = So nguyen) & Float ( Floating point numbers = So thuc)

print(type(1)) #int
print(type(0))
print(type(-10))

print(type(1.23)) #float
print(type(4E2)) #4*10(^2)

# [] Arithmetic: Cac phep toan: + - * /**/ // %

# [] Basic function (Ham co ban)
print(pow(10,3))
print(abs(-6.9)) # 6.9
print(round(6.69)) #7
print(round(5.458, 2)) #5.46
print(bin(512)) # '0b1000000000' --> binary format
print(hex(512)) # '0x200' --> hexadecimal format