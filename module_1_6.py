my_dyct = {'Radik': 1985, 'Albina': 1989, 'Ramazan': 2014, 'Rail': 2020} #переменная my_dyct со словарём из нескольких пар ключ-значений
print(my_dyct) #вывод на экран словаря my_dict
print(my_dyct.get('Albina')) #вывод на экран одного значения по существующему ключу
print(my_dyct.get('Medina', 'Её пока что, нету, но она в проекте... но жизнь интересная штука.')) #вывод на экран одного значения по отсутствующему из словаря my_dict без ошибки
my_dyct.update({'Medina': 2025, 'Yanbika': 2027}) #добавление ещё двух произвольных пары того же формата в словарь my_dict.
print(my_dyct) #вывод на экран обновленного словаря
del my_dyct['Yanbika'] #удаление пары в словаре по существующему ключу из словаря my_dict
print(my_dyct) #вывод на экран словаря my_dyct
my_set = {1, 22, 3, 24, 9, 2, 0, 22, 3, 24, 9, 2, 4, True, 'Famaly'} #переменная my_set со множеством, состоящее из разных типов данных с повторяющимися значениями
print(my_set) #вывод на экран множества my_set с уникальными значениями
print(my_set.add(2025)) #добавление нового произвольного элемента в множество my_set, которых ещё нет
print(my_set.add(2027)) #добавление нового произвольного элемента в множество my_set, которых ещё нет
print(my_set) #вывод на экран множества my_set с новыми значениями
print(my_set.discard(2)) #удаление элемента 2 из множества my_set
print(my_set) #вывод на экран измененного множества my_set
