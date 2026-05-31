set1={10,True,'jenny',1.11}
#print(set1)
set2={}
print(type(set1))
print(type(set2))
set3=set()
print(type(set3))

set4={10,56,89,90,'jenny',True,10}
set4.add(98)
print(set4)
print(len(set4))

#set4.remove(10)
#set4.discard(10)
#print(set4)

set4.pop()
print(set4)
