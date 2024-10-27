import multiprocessing

def producer(q):
    for i in range(10):
        q.put(i)

def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(item)

if __name__ == '__main__':
    queue = multiprocessing.Queue()  # creating queue object
    p1 = multiprocessing.Process(target=producer,args=(queue,))
    p2 = multiprocessing.Process(target=consume, args=(queue,))
    p1.start()
    p2.start()
    queue.put("sudh")
    p1.join()
    p2.join()