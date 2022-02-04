import threading
import multiprocessing
import time
import os


def first_task(data):
    proc = os.getpid()
    for i in data:
        print("first_task :", i, proc)


def second_task(data1, data2):
    proc = os.getpid()
    for i, j in zip(data1, data2):
        print("second_task :", i, j, proc)


task1 = threading.Thread(target=first_task, args=(range(5000),))
task2 = threading.Thread(target=second_task, args=(range(5), range(5)))

task1.daemon = False
task2.daemon = True

print("START")
task1.start()
task2.start()

time.sleep(0.02)
print("\nEND")