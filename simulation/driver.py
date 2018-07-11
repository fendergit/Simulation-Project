from models.job import SimpleJob
from models.queue import SimpleQueue
from models.stats import StatsAggregator
from utils.functions import *
from random import randint


file1 = open('results1-tmp.txt', 'w')
file2 = open('results2-tmp.txt', 'w')

for i in range(80, 170, 1):

    q1_capacity = 100
    q2_capacity = 12
    q3_capacity = i / 10

    q1_stats_agg = StatsAggregator(q1_capacity)
    q2_stats_agg = StatsAggregator(q2_capacity)
    q3_stats_agg = StatsAggregator(q3_capacity)

    q3 = SimpleQueue(q3_capacity, 1.0, "FCFS", None, q3_stats_agg)
    q1 = SimpleQueue(q1_capacity, 1.0/5, "SRJF", q3, q1_stats_agg)
    q2 = SimpleQueue(q2_capacity, 1.0/3, "Random", q3, q2_stats_agg)


    def ongoing_serve_enqueue(min_time, min_queue, max_time, max_queue, next_queue, equal_time=False):
        min_queue.serve(min_time)
        max_queue.serve(min_time)

        if next_queue.done_jobs.__len__() == 0:
            next_queue.serve(min_time)
        else:
            done_jobs = sorted(next_queue.done_jobs, key=lambda x: x[1], reverse=True)
            t = min_time
            for j in done_jobs:
                next_queue.serve(t-j[1])
                next_queue.enqueue(j[0])
                t = j[1]
            next_queue.serve(t)
            next_queue.done_jobs = []

        job = min_queue.generate_job()
        min_queue.enqueue(job)
        if equal_time:
            job = max_queue.generate_job()
            max_queue.enqueue(job)
        return max_time - min_time, 0


    next_arrival_q1 = next_arrival_q2 = 0

    while StatsAggregator.total_done_jobs < 5005000:
        if next_arrival_q1 == 0:
            next_arrival_q1 = generate_random_expo(7)
        if next_arrival_q2 == 0:
            next_arrival_q2 = generate_random_expo(2)

        if next_arrival_q1 < next_arrival_q2:
            next_arrival_q2, next_arrival_q1 = ongoing_serve_enqueue(next_arrival_q1, q1, next_arrival_q2, q2, q3)
        elif next_arrival_q1 > next_arrival_q2:
            next_arrival_q1, next_arrival_q2 = ongoing_serve_enqueue(next_arrival_q2, q2, next_arrival_q1, q1, q3)
        else:
            next_arrival_q1, next_arrival_q2 = ongoing_serve_enqueue(next_arrival_q2, q2, next_arrival_q1, q1, q3, True)


    pb1, lq1, wq1 = q1.stats.aggregate_results()
    file1.write(str(pb1) + ',' + str(lq1) + ',' + str(wq1) + '\n')

    pb3, t3, lq3 = q3.stats.aggregate_results2()
    file2.write(str(pb3) + ',' + str(t3) + ',' + str(lq3) + '\n')

    StatsAggregator.total_done_jobs = StatsAggregator.total_time = StatsAggregator.total_elapsed_time = 0

file1.close()
file2.close()
