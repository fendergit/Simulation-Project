from random import random
from math import exp, log, sqrt

def generate_random_expo(m):
    x = random()
    gen_rnd = log(1-x)/m * (-1.0)
    return gen_rnd


def calc_mean(nums):
    all_sum = 0
    for i in nums:
        all_sum += i
    mean = all_sum / float(nums.__len__())
    return mean


def calc_sample_variance(nums):
    mean = calc_mean(nums)
    all_sum = 0
    for i in nums:
        all_sum += (i - mean)**2
    var = all_sum / (float(nums.__len__()) - 1)
    S = sqrt(var)
    return S


def calc_precision(nums):
    R = nums.__len__()
    S = calc_sample_variance(nums)
    Y = calc_mean(nums)
    precision = 1.96 * S / (sqrt(R) * Y)
    return precision


def folan():
    file = open('results.txt', 'r')
    lines = file.readlines()
    print lines