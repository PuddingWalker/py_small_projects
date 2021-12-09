#########################################################################
# File Name: decorator.py
# Author: Pudding
# mail:qngskk@gmail.com
# Created Time: Tue Nov 23 20:05:09 2021
#########################################################################
#!/usr/bin/env python3


from datetime import datetime as dt
def now():
    print(dt.now())

def log(func):
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper

log(now)()

@log
def now():
    print("now is ", dt.now())

now()

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print("951223")

now()
print(now.__name__)
now = log('fuck')(now)
now()
print(now.__name__)


import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)
    return  wrapper

log(print)()

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn

