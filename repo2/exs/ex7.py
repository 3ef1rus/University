# сокращенный for in для list
# listt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_listt = []

# new_listt = [el for el in listt if el > 5]
# print(new_listt)

# сокращенный for in для set
# listt = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# new_listt = {}

# new_listt = {el*el for el in listt}
# print(new_listt)

# сокращенный for in для dic
# listt = {
#     'a': 1,
#     'b': 2,
#     'ac': 3,
# }
# new_listt = {}

# new_listt = {k: v*10 for k, v in listt.items()}
# print(new_listt)


# listt = ['a', 'b', 'c', 'd', 'f', 'e', 'g']


# new_listt = {k: v for k, v in enumerate(listt)}
# print(new_listt)

# dicc = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }

# dicc_up = {k.upper(): v for k, v in dicc.items()}
# print(dicc_up)

# listt = ['as', 'df', 'xzcv', 'xcvxzcvvvv']

# new_listt = [el for el in listt if len(el) > 3]
# print(new_listt)

# class Car:
#     def move(self):
#         print(f"Car is moving is {self}")

#     def stop(self):
#         print(f"Car is stopped is {self}")


# car1 = Car()
# car1.move()

# class Image:
#     def __init__(self, resolution, title, extendsion) -> None:
#         self.resolution = resolution
#         self.title = title
#         self.extendsion = extendsion

#     def resize(self, resolution):
#         self.resolution = resolution

#     def __str__(self):
#         return self.title + ' ' + self.extendsion + ' ' + self.resolution


# img1 = Image('1x1', 'home', 'img')
# img2 = Image('3x3', 'work', 'pdf')
# print(img1.resolution)
# img1.resize('100x100')

# print(img1.resolution)
# print(img2)
