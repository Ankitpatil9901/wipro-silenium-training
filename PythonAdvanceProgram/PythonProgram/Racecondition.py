import threading


#race condition is multiple thread access shared data without synchronisation

count = 0
lock = threading.Lock()

def increment():
    global count
    with lock:
        for _ in range(100000):
            count+=1


t1=threading.Thread(target=increment())
t2=threading.Thread(target=increment())

t1.start()
t2.start()

t1.join()
t2.join()

print(count)


# with lock - automatically acquires and release the lock for every thread




# with lock - automatically acquires and releases