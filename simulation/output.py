from utils.functions import *


def output_result2(policy):
    res_dir = 'results2-' + policy + '.txt'
    file = open(res_dir, 'r')
    lines = file.readlines()
    file.close()

    nums = [[], [], []]

    for line in lines:
        split_nums = line.rstrip().split(',')
        for i in range(nums.__len__()):
            nums[i].append(float(split_nums[i]))

    for i in range(9):
        k = [[], [], []]
        k[0] = nums[0][i*10:(i+1)*10]
        k[1] = nums[1][i*10:(i+1)*10]
        k[2] = nums[2][i*10:(i+1)*10]

        for num_list in k[1:]:
            mean = calc_mean(num_list)
            prec = calc_precision(num_list)
            print mean, prec


def output_result1():
    file = open('results1.txt', 'r')
    lines = file.readlines()
    file.close()

    nums = [[], [], []]

    for line in lines:
        split_nums = line.rstrip().split(',')
        for i in range(nums.__len__()):
            nums[i].append(float(split_nums[i]))


    for num_list in nums:
        mean = calc_mean(num_list)
        prec = calc_precision(num_list)
        print mean, prec
