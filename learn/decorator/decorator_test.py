#########################################################################
# File Name: decorator_test.py
# Author: Pudding
# mail:qngskk@gmail.com
# Created Time: Thu Nov 25 20:51:00 2021
#########################################################################
#!/usr/bin/env python3

# -*- coding: utf-8 -*-
import time, functools

#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("%s executed in %s" % (func.__name__, time.strftime("%Y-%m-%d %H:%M:%S")) )
        return func(*args, **kw)
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

