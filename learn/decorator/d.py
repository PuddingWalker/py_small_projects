#########################################################################
# File Name: d.py
# Author: Pudding
# mail:qngskk@gmail.com
# Created Time: Fri Nov 26 09:59:51 2021
#########################################################################
#!/usr/bin/env python3

import functools 

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')

today()
