#Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"
immutable_var= (1,2,3, [1,2,3], True, 'Привет')
print(immutable_var)
# immutable_var[8]=0 - недопустимая операция, кортеж не поддерживает обращение по элементам.

mutable_list=[3,5,6,'Список']
print(mutable_list)
mutable_list[2]=False
print(mutable_list)