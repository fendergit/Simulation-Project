from models.job import SimpleJob
from models.queue import SimpleQueue

random_queue = SimpleQueue(2, 1, "PS")
# print random_queue
job1 = SimpleJob(1)
job2 = SimpleJob(2)
job3 = SimpleJob(3)
job4 = SimpleJob(4)
job5 = SimpleJob(5)
# print job1
def printall():
    print random_queue, job5,job4,job3,job2,job1


random_queue.enqueue(job5)
printall()
random_queue.serve(2)
printall()
random_queue.enqueue(job4)
printall()
random_queue.serve(2)
printall()
random_queue.enqueue(job3)
printall()
random_queue.serve(2)
printall()
random_queue.enqueue(job2)
printall()
random_queue.serve(2)
printall()
random_queue.enqueue(job1)
printall()
random_queue.serve(2)
printall()
random_queue.serve(2)
printall()
random_queue.serve(2)
printall()
random_queue.serve(2)
printall()
