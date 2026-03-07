# Отфильтровать список чисел, оставив только числа, оканчивающиеся на 5.
# import random
# list_nums = random.sample(range(5, 45), random.randint(5, 15))
# print(list_nums)
# list_out = list(filter(lambda elem: str(elem).endswith('5'), list_nums))
# print(list_out)

# Преобразовать каждый элемент списка строк в список их гласных букв.
# vowels = 'aeouyi'
# my_list = ['apple', 'banana', 'cherry', 'date']
# list_out = []
# for elem in my_list:
#     list_vowels = [letter for letter in elem if letter.lower() in vowels]
#     list_out.append(list_vowels)
#
# print(list_out)

# Отфильтровать список строк, оставив только строки, содержащие только буквы.
# list_strings = ["apple", "42", "banana", "7", "cherry", "16", "date"]
# list_out = list(filter(lambda elem: not elem.isdigit(), list_strings))
# print(list_out)

# Преобразовать список списков в список их длин.
# list_out1 = []
# my_lists = [[1, 2, 3, 8], [4, 5], [7, 8, 9]]
# for elem in my_lists:
#     list_out.append(len(elem))
# print(list_out)
# list_out = list(map(len, my_lists))