# class Animal:
#     def move(self):
#         return "top top top"

#     def eating(self):
#         return "mef mef mef"

#     @staticmethod
#     def eat_and_move():
#         return "top mef top"


# wolf = Animal()
# # m1 = Animal.eating()  ошибка из-за того что не передается параметр селф тоесть не определет обьект
# m1 = Animal.eat_and_move()
# m2 = wolf.eat_and_move()
# print(m1)
# print(m2)


# class Animal:
#     count_animal = 0

#     def __init__(self, typee, name) -> None:
#         self.typee = typee
#         self.name = name
#         Animal.count_animal += 1

#     def move(self):
#         return "top top top"

#     def eating(self):
#         return "mef mef mef"

# class Animal:
#     count_animal = 0

#     def __init__(self, typee, name) -> None:
#         self.typee = typee
#         self.name = name
#         Animal.count_animal += 1

#     def move(self):
#         return "top top top"

#     def eating(self):
#         return "mef mef mef"

#     def __add__(self, other):  # магический метод для класса анимал
#         return (f"{self.typee} {other.typee}",
#                 f"fisrt name = {self.name}, second name = {other.name} ")

#     def __eq__(self, other):
#         if self.name == other.name:
#             return f"They name is the same"
#         else:
#             return f"They name is not the same"


# wof = Animal('dog', 'alex')
# lion = Animal('cat', 'joh')

# print(wof+lion)
# print(wof == lion)
