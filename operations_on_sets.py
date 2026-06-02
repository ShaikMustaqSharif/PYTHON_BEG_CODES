set1={'arshad','Rama','Greek'}
set2={'Greek','jiya','Aakash'}
print(set1.union(set2))
print(set1|set2)

set3={'Ram','Syam','jenny'}
set4={'jenny','jaya','Aakash'}
set5={'Ankur','Pradeep'}
print(set3.union(set4,set5))

set4.update(['jenny','Mohan'])
print(set4)
set4|=set5
print(set4ope)