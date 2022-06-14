# def debug(func):
#     def wrapper():
#         print("[DEBUG]: enter {}()".format(func.__name__))
#         return func()
#     return wrapper
# @debug
# ### 其实相当于 say_hello = debug(say_hello)
# def say_hello():
#     print("hello!")
# say_hello()

# import time
# def using_time(func):
#     def wrapper():
#         t1=time.time()
#         func()
#         t2=time.time()
#         print(t2-t1)
#     return wrapper
# @using_time
# def say_hello():
#     time.sleep(1)
#     print("hello!")
# say_hello()


import time
def using_time(func):
    def wrapper():
        t1=time.time()
        func(5)
        t2=time.time()
        print(t2-t1)
    return wrapper
@using_time
def say_hello(time_sleep):
    time.sleep(time_sleep)
    print("hello!")
say_hello()