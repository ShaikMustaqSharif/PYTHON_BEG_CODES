numbers=input("Enter list of numbers :")
# 34 45 12 -8 89 67
numbers_list=numbers.split()
count=0
for numbers in numbers_list:
    count+=1
print(f"the lenght of the list is :{count}")
for i in range(count):
    numbers_list[i]=int(numbers_list[i])
maximum_number=numbers_list[0]
for numbers in numbers_list:
    if numbers > maximum_number:
        maximum_number=numbers
print(f"The maximum number is :{maximum_number}")