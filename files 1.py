# 27. Создать программу для составления списка покупок. Реализовать добавление и удаление товаров из списка в файле.
# shopping_list = [
#     {"продукт": "Яблоки", "цена": 10},
#     {"продукт": "Молоко", "цена": 25},
#     {"продукт": "Хлеб", "цена": 15},
#     {"продукт": "Масло", "цена": 30},
#     {"продукт": "Сахар", "цена": 20},
#     {"продукт": "Яйца", "цена": 15},
#     {"продукт": "Мука", "цена": 18},
#     {"продукт": "Помидоры", "цена": 12},
#     {"продукт": "Огурцы", "цена": 10},
#     {"продукт": "Картошка", "цена": 8}
# ]
# import json
# def write_shopping_list(path, data):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             json.dump(data, my_file, ensure_ascii=False, indent=4)
#     except FileNotFoundError as ex:
#         print(ex)
# write_shopping_list('shopping_list.json', shopping_list)
#
# def read_file(path):
#     try:
#         with open(path, 'r+', encoding='utf-8') as my_file:
#             content = json.load(my_file)
#             return content
#     except FileNotFoundError as er:
#         print(er)
# resalt = read_file('shopping_list.json')
# print(resalt)
# product_to_add = input('введите ваш продукт ')
# product_price_add = float(input('и его цену '))
# product_input = {"продукт": product_to_add, "цена": product_price_add}  # Формируем словарь
# def add_product_to_shopping_list(path):
#     try:
#         with open(path, 'r+', encoding='utf-8') as my_file:
#             content = json.load(my_file)  # Загружаем текущий список покупок
#             content.append(product_input)  # Добавляем новый продукт к списку
#             my_file.seek(0)  # Перемещаем курсор в начало файла
#             json.dump(content, my_file, ensure_ascii=False, indent=4)
#     except FileNotFoundError as ex:
#         print(ex)
# add_product_to_shopping_list('shopping_list.json')