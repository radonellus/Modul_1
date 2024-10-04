immutable_var = 1, 2, 3, True, "Urban" #кортеж из нескольких элементов разных типов данных
print(immutable_var) #вывод кортежа immutable_var на экран
#immutable_var[0] = 777 попытка изменить первый элемент кортежа immutable_var
#print(immutable_var) ошибка TypeError: 'tuple' object does not support item assignment, так как элемент внутри кортежа не изменяем
mutable_list = [True, "Urban", 777] #переменная mutable_list и со списком из нескольких элементов
mutable_list[2] = "Курс Python, 2024 учебный год" #изменение 3-го элемента списка mutable_list
print(mutable_list) #вывод на экран измененный список mutable_list
