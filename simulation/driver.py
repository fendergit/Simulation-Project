from models.job import SimpleJob
from models.queue import SimpleQueue
from utils.functions import generate_random_expo
from random import randint

q = SimpleQueue(2, 1, "ps")
q1 = SimpleQueue(5, 1, "FCFS", q)
q2 = SimpleQueue(5, 1, "FCFS", q)


def printall(queue):
    print queue


def ongoing_serve_enqueue(min_time, min_queue, max_time, max_queue, next_queue, equal_time=False):
    min_queue.serve(min_time)
    max_queue.serve(max_time)

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

for i in range(5):
    if next_arrival_q1 == 0:
        next_arrival_q1 = randint(4, 6)
    if next_arrival_q2 == 0:
        next_arrival_q2 = randint(1, 3)
    # print next_arrival_q1, next_arrival_q2
    if next_arrival_q1 < next_arrival_q2:
        next_arrival_q2, next_arrival_q1 = ongoing_serve_enqueue(next_arrival_q1, q1, next_arrival_q2, q2, q)
    elif next_arrival_q1 > next_arrival_q2:
        next_arrival_q1, next_arrival_q2 = ongoing_serve_enqueue(next_arrival_q2, q2, next_arrival_q1, q1, q)
    else:
        next_arrival_q1, next_arrival_q2 = ongoing_serve_enqueue(next_arrival_q2, q2, next_arrival_q1, q1, q, True)


'''
        q1.serve(next_arrival_q1)
        q2.serve(next_arrival_q1)
        if q.done_jobs.__len__() == 0:
            q.serve(next_arrival_q1)
        else:
            done_jobs = sorted(q.done_jobs, key=lambda x: x[1], reverse=True)
            t = next_arrival_q1
            for j in done_jobs:
                q.serve(t-j[1])
                q.enqueue(j[0])
                t = j[1]
            q.serve(t)
        q1.enqueue(job)
        q1.serve(next_arrival_q2-next_arrival_q1)
        q2.serve(next_arrival_q2-next_arrival_q1)
        q2.enqueue(job)
'''


'''
fcfs_queue = SimpleQueue(2, 1, "FCFS")
ps_queue = SimpleQueue(2, 1, "FCFS", fcfs_queue)
#fcfs_queue = SimpleQueue(2, 1, "FCFS")
srjf_queue = SimpleQueue(2, 1, "SRJF", ps_queue)

jobs = []
for i in range(5):
    jobs.append(SimpleJob(i+1))

def printall(queue=ps_queue):
    print queue
    # for i in range(5, 0, -1):
    #     print jobs[i-1]


for i in range(5, 0, -1):
    ps_queue.enqueue(jobs[i-1])
    printall()
    ps_queue.serve(2)
    printall()
ps_queue.serve(2)
printall()
ps_queue.serve(2)
printall()
ps_queue.serve(2)
printall()
ps_queue.serve(2)
printall()
print fcfs_queue.done_jobs
'''