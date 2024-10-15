import json

# json_str = '{"id":133,"brand":"Nike","qty":84, "status":{"isForSale":true} }'

# sneak = json.loads(json_str)
# to_json = json.dumps(sneak, indent=1)
# print(to_json)


# ran_dic = {
#     'name': 'ivan',
#     'age': 21,
#     'alive': True
# }

# dic_in_json = json.dumps(ran_dic)

# print(dic_in_json)
# print(type(dic_in_json))

from pathlib import Path

# cwd = Path("C:/Users/10kmm/VScode prog/course Python/1/dganjo")
# cwd = Path('C:/')/'Users'/'10kmm'/'VScode prog'/'course Python'/'1'/'dganjo'
# if cwd.exists():
#     cwd.rmdir()
# else:
#     cwd.mkdir()

# text_file = open('text.txt', 'w')
# text_file.write("asdf asdf\n")
# text_file.write("second\n")
# text_file.close()
# текст выше аналогичен нижнему

# with open('text.txt', 'w') as text_file:
#     text_file.write("asdf asdf\n")
#     text_file.write("second\n")

# text_file = open('text.txt')
# print(text_file.read())
# text_file.close()
# текст выше аналогичен нижнему
# with open('text.txt') as text_file:
#     print(text_file.read())

# with open('text.txt', 'w') as text_file:
#     text_file.write("asdf asdf\n")
#     text_file.write("second\n")

# with open('text.txt') as text_file:
#     listt = text_file.readlines()
#     for el in listt:
#         print(el)


# my_file = Path('text.txt')

# if my_file.exists():
#     my_file.unlink()
# else:
#     file = open('text.txt', 'w')
#     file.close()
# if Path('C:/Users/10kmm/VScode prog/course Python/1/files/first.txt').exists():
#     Path('C:/Users/10kmm/VScode prog/course Python/1/files/first.txt').unlink()
# if Path('C:/Users/10kmm/VScode prog/course Python/1/files/second.txt').exists():
#     Path('C:/Users/10kmm/VScode prog/course Python/1/files/second.txt').unlink()
# if Path('C:/Users/10kmm/VScode prog/course Python/1/files').exists():
#     Path('C:/Users/10kmm/VScode prog/course Python/1/files').rmdir()
# Path("C:/Users/10kmm/VScode prog/course Python/1/files").mkdir()
# with open('C:/Users/10kmm/VScode prog/course Python/1/files/first.txt', 'w') as file:
#     file.write("First\n")
#     file.write("Second\n")
#     file.write("Thirs\n")

# with open('C:/Users/10kmm/VScode prog/course Python/1/files/second.txt', 'w') as file:
#     file.write("First\n")
#     file.write("Second\n")
#     file.write("Thirs\n")

# with open('C:/Users/10kmm/VScode prog/course Python/1/files/first.txt') as file:
#     print(file.readlines())

# with open('C:/Users/10kmm/VScode prog/course Python/1/files/second.txt') as file:
#     for el in file.readlines():
#         print(el)
# if Path('C:/Users/10kmm/VScode prog/course Python/1/files/first.txt').exists():
#     Path('C:/Users/10kmm/VScode prog/course Python/1/files/first.txt').unlink()
# if Path('C:/Users/10kmm/VScode prog/course Python/1/files/second.txt').exists():
#     Path('C:/Users/10kmm/VScode prog/course Python/1/files/second.txt').unlink()
# if Path('C:/Users/10kmm/VScode prog/course Python/1/files').exists():
#     Path('C:/Users/10kmm/VScode prog/course Python/1/files').rmdir()
