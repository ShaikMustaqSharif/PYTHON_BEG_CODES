name_1= input("what is  your name ?")
name_2 = input(" What is your name(her/she) ?")
combine_string = name_1 +name_2
lowercase_case_string = combine_string.lower()

t = lowercase_case_string.count('t')
r = lowercase_case_string.count('r')
u = lowercase_case_string.count('u')
e = lowercase_case_string.count('e')
true = t+r+u+e

l = lowercase_case_string.count('l')
o = lowercase_case_string.count('o')
v = lowercase_case_string.count('v')
e = lowercase_case_string.count('e')
love = l+o+v+e

love_score = int(str(love)+str(true))

if love_score < 10 or love_score >90:
    print(f"your score is {love_score} and you are together like coke and mentons")
elif love_score <40 or love_score > 50:
    print(f'your score is {love_score} and you are good to go')
else:
    print(f'your score is {love_score} and you are love')
