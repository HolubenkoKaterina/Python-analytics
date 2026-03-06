# Удвоить каждую букву в каждом элементе списка строк.
# my_strings = ['apple', 'banana', 'cherry', 'date']
# list_out = []
# for words in my_strings:
#     new_words = ''
#     for letter in words:
#         if not letter.isdigit():
#             new_words += letter * 2
#     list_out.append(new_words)
# print(list_out)
# list_out = [''.join(letter * 2 for letter in word if not letter.isdigit()) for word in my_strings]

# Отфильтровать список строк, оставив только строки, содержащие букву 'a'.
# my_strings = ['apple', 'banana', 'cherry', 'date']
# list_out = list(filter(lambda  elem: 'a' in elem, my_strings))
# print(list_out)

# Преобразовать каждый элемент списка строк в список букв.
# my_strings = ['apple', 'banana', 'cherry', 'date']
# list_letter_of_elem = []
# for elem in my_strings:
#     words = [letter for letter in elem]
#     print(words)

# Отфильтровать список чисел, оставив только числа, большие 10.
# import random
# list_numbers = list(random.sample(range(5, 40), random.randint(10, 15)))
# print(list_numbers)
# list_out = list(filter(lambda elem: elem > 10, list_numbers))
# print(list_out)

# # Умножить каждый элемент списка на его индекс.
# import random
# list_numbers = list(random.sample(range(5, 40), random.randint(10, 15)))
# list_out = [elem * index for index, elem in enumerate(list_numbers)]
# print(list_out)

# # Отфильтровать список строк, оставив только палиндромы.
# list_strings = ["radar and level", "A man, a plan, a canal: Panama",  "Was it a car or a cat I saw?",
#                  "Evil is a name of a foeman, as I live.", 'lisa', 'miska']
# list_out = []
# for elem in list_strings:
#     clean_elem = elem.lower().split()
#     if clean_elem != clean_elem[::-1]:
#         list_out.append(elem)
# print(list_out)

# Преобразовать список имен в список инициалов (например, "John Smith" в "J. S.").
# names = ["John Smith", "Jane Doe", "Michael Johnson"]
# initials = []
# for name in names:
#     parts = name.split()
#     first_initial = parts[0][0].upper()
#     last_initial = parts[1][0].upper()
#     full_initials = f"{first_initial}. {last_initial}."
#     initials.append(full_initials)
# print(initials)

