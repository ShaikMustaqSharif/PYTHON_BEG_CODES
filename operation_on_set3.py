set1={'Ram','shyam','Jenny'}
set2={'Jenny','Jiya','Akash'}
set3={'Anukar','Pradeep','Ram'}
print(set1.difference(set2))
print(set1-set2)
print(set1.difference('Mohan','Shiva'))

print(set1.difference(set2,set3))

set1.difference_update((set2))
print(set1)

print(set1.symmetric_difference(set2))
print(set1^set2^set3)
