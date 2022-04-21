from itertools import count
from typing import Counter



persons = [
    {'name': 'Anna', 'age': 25, 'gender': 'female'},
    {'name': 'Lena', 'age': 12, 'gender': 'female'},
    {'name': 'Nastya', 'age': 33, 'gender': 'female'},
    {'name': 'Angelina', 'age': 30, 'gender': 'female'},
    {'name': 'Anna', 'age': 22, 'gender': 'female'},
    {'name': 'Anna', 'age': 40, 'gender': 'female'},
    {'name': 'Ira', 'age': 11, 'gender': 'female'},
    {'name': 'Polina', 'age': 17, 'gender': 'female'},
    {'name': 'Oksana', 'age': 18, 'gender': 'female'},
    {'name': 'Anna', 'age': 8, 'gender': 'female'},
    {'name': 'Yana', 'age': 43, 'gender': 'female'},
    {'name': 'Kira', 'age': 18, 'gender': 'female'},
    {'name': 'Nastya', 'age': 25, 'gender': 'female'},
    {'name': 'Tamara', 'age': 31, 'gender': 'female'},
    {'name': 'Rita', 'age': 39, 'gender': 'female'},
    {'name': 'Sveta', 'age': 25, 'gender': 'female'},
    {'name': 'Anna', 'age': 22, 'gender': 'female'},
    {'name': 'Nastya', 'age': 28, 'gender': 'female'},
    {'name': 'Lera', 'age': 19, 'gender': 'female'},
    {'name': 'Sara', 'age': 10, 'gender': 'female'},
    {'name': 'Alex', 'age': 44, 'gender': 'male'},
    {'name': 'Dima', 'age': 33, 'gender': 'male'},
    {'name': 'Fedor', 'age': 38, 'gender': 'male'},
    {'name': 'Nikita', 'age': 32, 'gender': 'male'},
    {'name': 'Alex', 'age': 25, 'gender': 'male'},
    {'name': 'Foma', 'age': 7, 'gender': 'male'},
    {'name': 'Evgeniy', 'age': 25, 'gender': 'male'},
    {'name': 'Alex', 'age': 12, 'gender': 'male'},
    {'name': 'Kiril', 'age': 27, 'gender': 'male'},
    {'name': 'Mihail', 'age': 30, 'gender': 'male'}
]

a = len (persons)
print (f'В данном списке {a} человек.') #Колличество записей, а соответственно количество людей

b = ([gen1['gender'] for gen1 in persons])
male = b.count('male')
female = b.count('female')
print (f'Из них {female} женщин и {male} мужчин.')

c = ([age['age'] for age in persons])
age = len([item for item in c if item >= 18])
print (f'Количество совершенно летних людей = {age}')

d = ([name['name'] for name in persons])
print (d)   #Список всех имен


e = sorted(set([age['age'] for age in persons]))
print (e)  #Список всех возрастов без повторений

f = Counter([name['name'] for name in persons]).most_common(3)
for most_name in f:
    print(f'Имя {most_name[0]}, встречается {most_name[1]} раз(-а).')

over_35 = [i['name'] for i in persons if i['age'] >= 35 and i['gender'] == 'male']
print (over_35)   