# name = 'Ivan'
# age = 21
# hobby = 'prog'
# st = f"My name is {name}, im {age}, i'd likes {hobby}"
# print(st)

# def greeting(greet):
#     return lambda name: f"{name},{greet}"


# morning = greeting("Good morning")
# print(morning('Ivan'))


# try:
#     10+'0'
# except TypeError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)
# print(0)

# try:
#     10/0
# except Exception as e:  # exctption общий класс ошибок и будет выводить большенсво ошибок без повторения except
#     print(e)

# print(0)

# def image_info(image):
#     if 'image_title' not in image or 'image_id' not in image:
#         raise TypeError('Keys image_title or image_id not in dic')
#     return f"Image '{image['image_title']}' has id {image['image_id']}"


# image = {
#     'image_title': 'my cat',
#     # 'image_id': '5136'
# }
# try:
#     print(image_info(image))
# except TypeError as e:
#     print(e)

# def ddk(name, age):
#     return f'Ego name {name} and age {age}'


# my_list = [{'name': 'ivan', 'age': '21'},
#            {'name': 'joh', 'age': '23'},
#            {'name': 'evgen', 'age': '65'}]

# dic1, dic2, dic3 = my_list


# print(ddk(**dic1))
# print(ddk(**dic2))
# print(ddk(**dic3))

# def rout_info(args):
#     if ('distant' in args) and type(args['distant'] == int):
#         return f"distant oyou {args['distant']}"
#     elif ('speed' in args) and ('time' in args):
#         return f"distant is you dis {args['speed']*args['time']}"
#     else:
#         return "no distant info"


# dist = {
#     'distant': 152
# }
# dist2 = {
#     'speed': 152,
#     'time': 3
# }
# dist3 = {
#     'age': 152

# }
# print(rout_info(dist))
# print(rout_info(dist2))
# print(rout_info(dist3))
