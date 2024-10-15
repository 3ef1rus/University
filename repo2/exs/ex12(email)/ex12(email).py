from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

my_email = EmailMessage()
# добавление шаблона хтмл ниже и замена переменных на значения внутри файла
html_template = Template(Path('templates/index.html').read_text())
html_content = html_template.substitute({'name': 'Ivan', 'date': 'tomorrow'})

my_email['from'] = 'ivan@gmail.com '
my_email['to'] = 'lesx@gmail.com'
my_email['subject'] = "Look at the screen"
my_email.set_content(html_content, 'html')
# ниже добавление картинки как приложения к сообщению
with open('images\image.jpg', 'rb') as img:
    img_date = img.read()
    my_email.add_attachment(img_date, maintype='image',
                            subtype='jpg', filename='image.jpg')

with smtplib.SMTP(host='localhost', port='2525') as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls() шифровка данных если нужна
    # smtp_server.login(user='',password='')если нужна авторизация
    smtp_server.send_message(my_email)
    print("Email was sent!")

# docker run --rm -it -p 3000:80 -p 2525:25 rnwood/smtp4dev
