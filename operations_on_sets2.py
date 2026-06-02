set1={'Ram','Syam','jenny'}
set2={'jenny','jaya','Aakash'}
set3={'Ankur','Pradeep'}
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.intersection(set2,set3))
print(set1&set2)
print(set1&set2&set3)

set1.intersection_update(set2)
print(set1)