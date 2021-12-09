#########################################################################
# File Name: d1.py
# Author: Pudding
# mail:qngskk@gmail.com
# Created Time: Thu Nov 25 20:55:23 2021
#########################################################################
#!/usr/bin/env python3

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("begin call %s():" % func.__name__)
        s = func(*args, **kw)
        print("end call %s():" % func.__name__)
        return s
    return wrapper

def snow():
    print("Tu eres mi esposa")
log(snow)()

@log
def snow():
    print("Tu eres muy bonito")

snow()

#log2(text, t = 'ddd'):    def decorator(func):        def wrapper(*args, **kw):            print('begin %s %s() text:' % (text, func.__name__))            s = func(*args, **kw)            print('end %s %s() text:' % (text, func.__name__))            print(t)            return s        return wrapper    return decorator@log@log2('exe')def now():    print('2021/11/24')now()

print()

def log(func, text = 'execute'):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("begin %s %s():" % (text, func.__name__))
        s = func(*args, **kw)
        print("end %s %s()" % (text, func.__name__))
        return s
    return wrapper

@log
def miss():
    print("Yo quiero tu")

miss()
