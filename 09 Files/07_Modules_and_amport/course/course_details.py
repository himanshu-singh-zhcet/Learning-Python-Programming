import os, sys    # te wala code humne files and directory ko track karne ke liye likha hai 
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),'..')))


from payment import payment_details

def course():
    print("this is my course details")

course()
payment_details.payment()
