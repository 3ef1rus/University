def dec_fun(org_fun):
    def wrapper(*args, **kwargs):
        print("something change")  # действия до вызова функ
        a, b = args
        a = a+b*10
        b = b+a*100
        args = a, b
        result = org_fun(*args, **kwargs)
        print("alert if need")  # действия после вызова функ
        return result
    return wrapper


@dec_fun
def my_func(a, b):
    print('Hello')
    return [a, b]


res = my_func(515, 100)
print(res)

# def log_fun(fn):
#     def wrapper_fn(*args, **kwargs):
#         print(
#             f"func name is {fn.__name__} and args this fun is {args} and {kwargs}")
#         result = fn(*args, **kwargs)
#         print(f"func result : {result}")
#         return result
#     return wrapper_fn


# @log_fun
# def mul(a, b):
#     return a*b


# print(mul(5, 2))


# def valid_fun(fn):
#     def wrapper(*args, **kwargs):

#         for el in [*args, *kwargs.values()]:
#             if type(el) != int and type(el) != float:
#                 raise TypeError(f"Type arg {el} is {type(el)}",
#                                 "All args need int or float")

#         return fn(*args, **kwargs)
#     return wrapper


# @valid_fun
# def sum_num(a, b):
#     return a+b


# try:
#     print(sum_num(12, 33))
#     print(sum_num(b=12.5, a="33.8"))
# except Exception as e:
#     print(e)

# def is_user_auth():
#     return False


# def check_user_auth(fn):
#     def wrapper(*args, **kwargs):
#         if is_user_auth():
#             print("User is auth")
#             return fn(*args, **kwargs)
#         else:

#             raise Exception("User is not auth")

#     return wrapper


# @check_user_auth
# def do_sen_job():
#     # чтото произойдет если польз авторизован
#     print("something doing")


# try:
#     do_sen_job()
# except Exception as e:
#     print(e)
