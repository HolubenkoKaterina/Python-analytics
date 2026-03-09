# Проверить, все ли строки в списке имеют длину более 5 символов, используя all.
# text = ['my mind', 'coffe is fu', 'mama help me!']
# for element in text:
# check = all(len(element) > 5 for element in text)
# if check == True: print(True)
# if check != True: print(False)

# Проверить, все ли элементы в списке являются четными числами, используя all.
# list1 = [4, 5, 6, -18]
# check = all(elem % 2 == 0 for elem in list1 )
# print(check)

# Проверить, есть ли хотя бы одно нечетное число в списке, используя any.
# list1 = [4, 5, 6, -18]
# check = any(elem < 0 for elem in list1)
# print(check)

# Проверить, есть ли хотя бы один элемент в списке, удовлетворяющий определенному условию, используя any.
# list1 = [4, 5, 6, 18]
# check = any(elem < 0 and elem % 2 == 0 for elem in list1)
# print(check)

# Проверить, есть ли хотя бы одна пара элементов с одинаковыми индексами, которые больше заданного порога.
# list1 = [5, 5, 2, 3]
# list2 = [10, 5, 2, 13]
# some_number = int(input("введите ваше число..."))
# check = any(elem > some_number and element > some_number for elem, element in zip(list1, list2))
# print(check)

# Написать функцию, которая объединяет несколько списков в один, используя zip.
# list1 = [5, 15, 20, 25]
# list2 = [10, 15, 20, 25]
# resalt = list(zip(list1, list2))
# print(resalt)

# Создать новый список, содержащий только четные элементы из двух списков, объединенных через zip.
# list1 = [5, 15, 20, 25]
# list2 = [10, 15, 20, 25]
#
# Проверить, все ли элементы в списке удовлетворяют определенному условию, используя all.
# list1 = [5, 15, 20, 25]
# check = all(elem % 2 == 0 for elem in list1)
# print(check)

# Проверить, все ли слова в списке начинаются с заглавной буквы, используя all.
# text = ['My Mind', 'Coffe Is Fu', 'Mama Help Me!']
# check = all(elem.istitle() for elem in text)
# print(check)

# Проверить, все ли элементы в списке находятся в диапазоне от 10 до 20, используя all.
# list1 = [15, 20, 19]
# check = all(elem in range(10, 21) for elem in list1)
# print(check)

