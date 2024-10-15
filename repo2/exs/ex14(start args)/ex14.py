# from array import array

# my_int_arr = array('i', [4, 56, 1, 24, 6])

# # my_int_arr.append('abc')  аррай только для однотипных данных


# with open('my_arr_int.bin', 'wb') as file:
#     my_int_arr.tofile(file)


# new_arr = array('i')
# with open('my_arr_int.bin', 'rb') as file:
#     while True:
#         try:
#             value = array('i')
#             value.fromfile(file, 1)  # Считываем одно значение
#             if not value:
#                 break  # Прерываем цикл, если достигнут конец файла
#             new_arr.extend(value)
#         except EOFError:
#             break  # Обработка ошибки конца файла
# print(new_arr)

# import sys
# # аргументы запуска программы
# sys.argv

# могут быть разные и что бы прочитать их используется верх а что бы присвоить низ
# filename,username,password=sys.argv
