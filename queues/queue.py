from jobs.job import SimpleJob as job
from random import randint

class SimpleQueue():

    capacity = 100
    service_time = 1
    policy = "Random"
    length = 0
    jobs = []
    current_servicing_job = None

    def __init__(self, capacity, service_time, policy):
        self.capacity = capacity
        self.service_time = service_time
        self.policy = policy


    def enqueue(self, job):
        if self.length < self.capacity:
            self.jobs.append(job)
            self.length += 1


    def serve(self, t):
        if self.policy == "Random":
            while t > 0:
                extra_t = self.current_servicing_job.consume(t)
                for job in self.jobs:
                    job.waiting_time += t - extra_t
                if self.current_servicing_job.is_done:
                    self.choose_job_to_service()
                t = extra_t


    def choose_job_to_service(self):
        if self.policy == "Random":
            job = self.jobs.pop(randint(0, self.length - 1))
            self.current_servicing_job = job
