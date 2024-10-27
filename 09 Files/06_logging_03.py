import logging
logging.basicConfig(filename="test2.log",level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')
l1 = [1,2,3,34,4,[2,3,4],"sudh","kumar"]
l1_int = []
l1_str = []
for i in l1:
    logging.info("we are iterating through our list and our local variable is i"+str(i))
    if type(i) == list:
        logging.info("i m inside if statement and i m trying to list type")
        for j in i:
            logging.info("i m inside another for loop for list inside the list element")
            if type(j) == int:
                logging.info("i m inside if statement")
                l1_int.append(j)
    elif type(i) == int:
        l1_int.append(i)
    else:
        if type(i) == str:
            l1_str.append(i)
logging.info("my final result for int is {l1} and str is {l2}".format(l1 = l1_int,l2=l1_str))