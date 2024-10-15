import sqlite3

DB_NAME = "sqllite_db.db"


with sqlite3.connect(DB_NAME) as db:
    sql_req = "SELECT * FROM courses"
    # for el in db.execute(sql_req):
    #     print(el)
    date_from_db = db.execute(sql_req)
    print(date_from_db.fetchall())

# Добавление данных в ДБ
# courses = [
#     (233, "JS course", 333, 2341),
#     (3, "C++ course", 412, 111),
#     (11, "Django course", 42, 555),
#     (1233, "HTNL course", 11, 34)
# ]
# with sqlite3.connect(DB_NAME) as db:
#     sql_req = "INSERT INTO courses VALUES (?,?,?,?)"
#     for el in courses:
#         db.execute(sql_req, el)
#     db.commit()
# создание новой таблицы
# sql_req = """CREATE TABLE IF NOT EXISTS courses(
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         student_qty integer,
#         reviews_qty integer);"""
# db.execute(sql_req)
