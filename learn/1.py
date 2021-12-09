#########################################################################
# File Name: 1.py
# Author: Walker
# mail:qngskk@gmail.com
# Created Time: Tue Dec  7 14:58:24 2021
#########################################################################
# !/usr/bin/env python3
import time
import threading
import json
import requests


def sum(*numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total


x = 200


def print_value():
    global x
    x = 100


print('函数中x = {0}'.format(x))
print_value()
print('全局变量x = {0}'.format(x))
# 输出结果：
# 函数中x=100
# 全局变量x=100

arr = [n for n in range(100)]


def biger50(n):
    return True if n > 50 else False


print(list(filter(biger50, arr)))

r = requests.get('https://cn.bing.com/')
# print(r.status_code)
# print(r.content)

# print(r.content.decode())
# json.loads(r.content)


def thread_body():
    # current
    t = threading.current_thread()
    for n in range(5):
        # cur
        print('{0} th excute thread {1}.'.format(n, t.name))
        # thread sleep
        time.sleep(2)
    print('thread {0} Done.'.format(t.name))


# main thread
# create th obj 1
t1 = threading.Thread(target=thread_body)
# obj 2
t2 = threading.Thread(target=thread_body, name="MyThread")
# active thread t1
# t1.start()
# active thread t2
# t2.start()


class SmallThread(threading.Thread):
    def __init__(self, name=None):
        super().__init__(name=name)

    #

    def run(self):
        # current
        t = threading.current_thread()
        for n in range(5):
            # cur
            print("{0} th excute {1}".format(n, t.name))
            # sleep
            time.sleep(2)
        print(f'thread{t.name} done.')


# main
# crt t1
#t1 = SmallThread("t1")
# crt t2
#t2 = SmallThread("t2")
# launch
# t1.start()
# t2.start()

value = []


def thread_body():
    print(f'{threading.current_thread().name} starting...')
    for n in range(4):
        print(f'{n}_th {threading.current_thread().name} running...')
        value.append(n)
        time.sleep(2)
    print(f'{threading.current_thread().name} done.')


#print("main ....")
#t1 = threading.Thread(target=thread_body)
# t1.start()
# block
# t1.join()
#print('value = {0}'.format(value))
#print('main continue')

# thread stop
isrunning = True


# work thread body
def workthread_body():
    while isrunning:
        # thread beginning to work
        print(f'{threading.current_thread().name} is working...')
        # thread sleep
        time.sleep(5)
    print(f'{threading.current_thread().name} Finished its job.')


# control thread body
def controlthread_body():
    global isrunning
    while isrunning:
        # input stop cmd from standard input(keyboard)
        command = input('Input Stop Command: ')
        if command == 'exit':
            isrunning = False
            print('control thread done.')


# main
# crt work thread obj workthread
workthread = threading.Thread(target=workthread_body)
#
workthread.start()

# crt ctrl thread obj controlthread
controlthread = threading.Thread(target=controlthread_body)
controlthread.start()
