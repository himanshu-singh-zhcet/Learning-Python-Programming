import multiprocessing
def sender(conn,msg):
    for i in msg:
        conn.send(i)
    conn.close()

def receive(conn):
    while True:
        try:
            msg = conn.recv()
        except Exception as e:
            print(e)
            break
        print(msg)

if __name__ == '__main__':
    msg  = ["this is","a good","boy","of my school"]
    parent_conn,child_conn = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=sender,args=(child_conn,msg))
    p2 = multiprocessing.Process(target=receive,args=(parent_conn,))
    p1.start()
    p2.start()
    p1.join()
    child_conn.close()
    p2.join()
    child_conn.close()