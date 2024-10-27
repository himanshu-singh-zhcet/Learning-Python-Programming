import multiprocessing
def sqaure(n):
    return n**2

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        out = pool.map(sqaure, [1,2,3,4,5,6,7,8,9])  # pool yhaa pr is 4 process main baat dega 
        print(out)
