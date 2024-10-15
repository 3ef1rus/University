# from zipfile import ZipFile
# from pathlib import Path

# Path.mkdir('zipfile', exist_ok=True)
# with open('zipfile/file1.txt', 'w') as file:
#     file.write('hello')
# with open('zipfile/file2.txt', 'w') as file:
#     file.write('hello second')

# with ZipFile('zipfile.zip', 'w') as zip_file:
#     for file in Path('zipfile').iterdir():
#         print(file)
#         zip_file.write(file)

# with ZipFile('zipfile.zip') as zip_file:
#     zip_file.extractall('unzipfile')

# import csv

# with open('text.csv', 'w') as csv_file:
#     write = csv.writer(csv_file)
#     write.writerow(['user_id', 'user_name', 'time_user'])
#     write.writerow(['321', 'ivan', '100'])
#     write.writerow(['221', 'joh', '333'])
#     write.writerow(['333', 'mike', '444'])
# with open('text.csv') as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(line)

# from datetime import date
import re

# проверка почты


def email_check(mail):
    mail_check = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    mail_patt = re.compile(mail_check)
    validation = 'valid' if mail_patt.fullmatch(mail) else "not valid"
    return (mail, validation)

# print(email_check('sadf@dsaf.asdf'))


# def pass_check(passw):
#     pass_checkk = re.compile(
#         r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$')
#     validation = 'valid' if pass_checkk.fullmatch(passw) else "not valid"
#     return (passw, validation)


# email = input("Ввведите почту: ")
# passw = input("Ввведите пароль: ")

# print(email_check(email))
# print(pass_check(passw))
