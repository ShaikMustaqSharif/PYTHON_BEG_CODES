count=1
while count<=5:
    print(count)
    count+=1
print("out from loop")
print()
count=5
while count>0:
    print(count)
    count-=1
print("out from loop")
print()
count=5
while count>0: print(count); count-=1
print("out from loop")

print()
print()

count=5
while count>0:
    print(count); count-=1;
    if count ==3:
        break
    else:
        print("in else block")
print("out from loop")

number =int(input("Enter a number(-1 to quit):"))
while number  !=-1:
    print(number)
    number = int(input("Enter a number(-1 to quit):"))
else :
    print("in else block")
print("out from loop")



