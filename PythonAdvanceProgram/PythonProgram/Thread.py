# thread - execution of tasks
# multithread - execution of many task at a time -- concurrent execution
# Multiprocessing

# Process - execution unit
# threads- light weight unit inside the process

# simple thread

import threading
import time

def task():
    print("Thread Started")
    time.sleep(2)
    print("Thread finished")

t = threading.Thread(target=task)
t.start()
t.join()

print("Thread terminated")





