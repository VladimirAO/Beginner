#Практическое задание по теме: "Словари и множества"

my_dict={'Alex':1916, 'Ustas':1925, 'Borman':1913, 'Shtirlitc': 1914}
print('Словарь:',my_dict)
print('Присутствует значение:',my_dict['Ustas'], ' Ключ "Schlag":', my_dict.get('Schlag'))
my_dict.update({'Schlag':1909, 'Wolf':1921})
a=my_dict.pop('Wolf')
print('Удалённое значение:',a)
print('Изменённый словарь:',my_dict)
my_set={1,1,1,2,'Set',3,True,(1,2,3),4,4,5,5,5,5,6,1,1,1,2,'Set',3,True,(1,2,3),4,4,5,5,5,5,6,}
print('Множество:',my_set)
my_set.add(10)
my_set.add(12)
my_set.remove('Set')
print('Изменённое множество:',my_set)
