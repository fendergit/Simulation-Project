from random import random
from math import exp, log

def generate_random_expo(m):
    x = random()
    gen_rnd = log(1-x)/m * (-1.0)
    return gen_rnd

