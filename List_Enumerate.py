'''
Docstring for List & Enumerate
List trong Python la 1 dang du lieu cho phep luu tru nhieu kieu du lieu khac nhau trong mot chuoi va chung ta co the truy
xuat den cac phan tu ben trong no thong qua vi tri cua phan tu do trong list

Ngon ngu khac: C/C++, Java, List trong Python = Mang(Array)

'''
'''
2. Access elements: Truy cap den cac gia tri trong list
'''

my_list =[1,2,'3',True]
print(len(my_list))

print(my_list[2]) # look the index element number 2
print(my_list.index(2)) #look for where the number 2 is

my_list1 =[1,2,3,3,3,'3','3',True]
print(my_list1.count(3)) #count number 3

for item in my_list1:
    print(item)

#Python's built-in enumerate function
# allow us to loop over a list and retrieve both the index and the value of each item in the list
presidents = ['Washington', 'Adam', 'Jefferson', 'Madison', 'Monroe', 'Adams', 'Jackson']

print(presidents)
for index, president in enumerate(presidents):
    print(f"President #{index}: {president}")

    
print(presidents)
for index, president in enumerate(presidents, start = 1):
    print(f"President #{index}: {president}")

#Slicing
# : is called slicing and has the format [start: end : step]
my_list2 = [1,2,'3', True]

print(my_list2[1:])
print(my_list2[:1])
print(my_list2[::2]) #step by 2
print(my_list2[::-1]) #reverse 

# List operations & Useful methods
# Add to list
print(my_list + [100,'Huyentran'])
print(my_list.append(200)) # only add 1 value
print(my_list)

print(my_list.extend([300, "HT"])) # add multiple

print(my_list.insert(3,4)) # insert(index, value)
print(my_list)

#remove from my list
print(my_list.pop()) #remove the last element in the list
print(my_list)

print(my_list.pop(1)) #remove by index
print(my_list)

my_list = [1, 2, '3', 4, 2,2 ,True, 200, 300]
my_list.remove(2) #it just removes the first element it sees
print(my_list)


del my_list[3] # index
print(my_list)

#sorting
myl = [1,2,8,4,5,7]
myl.sort()
print(myl)

myl.sort(reverse= True)
print(myl)