# screen = ('1920', '1080')

# size = f"{screen[0]}x{screen[1]}" if len(screen) == 2 and type(
#     screen[0]) == str and type(screen[1]) == str else 'Error'

# print(size)

# screen = ('1920', '1080')

# if len(screen) == 2 and type(screen[0]) == str and type(screen[1]) == str:
#     size = f"{screen[0]}x{screen[1]}"
# else:
#     size = 'Error'

# print(size)

# leng = 100
# length = "string is long" if leng > 79 else "string is short"
# print(length)


# def dic_to_lis(arg):
#     listr = []
#     for k, v in arg.items():
#         if type(v) == int:
#             v *= 2
#         listr.append((k, v))
#     return listr


# di = {'id': 1234,
#       'as': 333,
#       'ff': 423
#       }

# print(dic_to_lis(di))

# def filter_list(lis, typ):
#     conv_list = []
#     for i in lis:
#         if type(i) == typ:
#             conv_list.append(i)

#     return conv_list


# listtt = [1, 2, 3]
# print(filter_list([1, 2, 3, '22', 'asdf', True], int))

# def filt_list(list_con, typ):
#     def chek_elm_typ(elm):
#         return type(elm) == typ
#     return list(filter(chek_elm_typ, list_con))


# print(filt_list([1, 2, '3', '4', 'qw'], int))

# import random

# ran_num = random.randint(1, 5)

# while True:
#     num = int(input("Enter num from 1 to 5 : "))
#     if num == ran_num:
#         print("Yes u right")
#         break
#     print("Try again")
#     continue

# while True:

#     try:
#         first = float(input("Enter first num : "))
#         second = float(input("Enter second num : "))
#         first/second
#     except Exception as e:
#         print(e)
#         print("Try again")
#         continue
#     print(first/second)
#     choose = input("U want continue Y/N : ")
#     if choose.upper() == 'Y':
#         continue
#     if choose.upper() == 'N':
#         print("See u again")
#         break
