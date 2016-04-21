# encoding: utf-8

import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

for x in range(0, 10):
    print(id_generator())