import random
import string
import datetime
from time import sleep

letters = string.ascii_lowercase
constant = ''.join(random.choice(letters) for i in range(10))

while True:
    sleep(5)
    timer = datetime.datetime.now()
    print (timer, ": ", constant)



