import logging
logging.basicConfig(filename="test.log",level=logging.INFO)
logging.info("log this line of execution")
logging.debug("this message would not be log")
logging.warning("this is my warning message")
logging.error("this is my error")
logging.critical("this is my critical message")
logging.shutdown()