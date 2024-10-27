import multiprocessing
def test():
    print("this is my multiprocessing program")

if __name__ == '__main__':
    m = multiprocessing.Process(target=test)
    print("this is my main program")
    m.start()
    m.join()