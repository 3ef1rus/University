# def sum_nums(*args):# *args принимает любое количество аргументов
#                     # и конвертирует их в tuple
#     return sum(args)


# print(sum_nums(1,2,3,4))

# def sum_nums(**args):# **args принимает любое количество аргументов
#                      # и конвертирует их в dict

#     return print(args)

# sum_nums(name=12,age=33)

# def marge_list_to_dict(list1,list2):
#     return dict(zip(list1,list2))


# list1=['name','age']
# list2=['Ivan',21]
# my_dict=marge_list_to_dict(list1,list2)
# print(my_dict)


# def marge_list_to_dict(list1, list2):
#     return dict(zip(list1, list2))


# my_dict = marge_list_to_dict(list1=['name', 'age'], list2=['Ivan', 21])
# print(my_dict)


# def update_car_info(**info):
#     info['is_available']=True
#     return info

# print(update_car_info(brand='niva',price=555))
