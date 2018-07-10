from random import randint
from job import SimpleJob
from stats import StatsAggregator
from utils.functions import generate_random_expo

class SimpleQueue():


    def __init__(self, capacity=100, service_time=1, policy="Random", next_queue=None, stats_agg=None):
        self.capacity = capacity
        self.service_time = service_time
        self.policy = policy
        self.next_queue = next_queue
        self.length = 0
        self.jobs = []
        self.current_servicing_job = None
        self.done_jobs = []
        self.total_elapsed_time = 0
        self.stats = stats_agg


    def __str__(self):
        res_str = "\nlength " + str(self.length) + " " + \
              "jobs " + str(self.jobs) + " " + \
              "current " + str(self.current_servicing_job) + "\n"
        for job in self.jobs:
            res_str += job.__str__() + "\n"
        return res_str



    def enqueue(self, job):
        if StatsAggregator.total_done_jobs > 5000:
            self.stats.num_incoming_jobs += 1
            self.stats.length += self.length
            self.stats.num_length_reports += 1

        if self.length < self.capacity:
            self.length += 1

            if self.policy == "Random" or self.policy == "PS" or self.policy == "FCFS":
                self.jobs.append(job)

            if self.policy == "SRJF":
                if self.current_servicing_job is not None:
                    current_remaining_time = self.current_servicing_job.total_time_needed - self.current_servicing_job.consumed_time
                    if job.total_time_needed < current_remaining_time:
                        self.jobs.append(self.current_servicing_job)
                        self.current_servicing_job = job
                    else:
                        self.jobs.append(job)
                else:
                    self.jobs.append(job)

            job.next_queue = self.next_queue
            job.current_queue = self
            if StatsAggregator.total_done_jobs > 5000:
                self.stats.num_enqueue_jobs += 1
            return True

        job.is_blocked = True
        if StatsAggregator.total_done_jobs > 5000:
            self.stats.blocked_jobs += 1
        return False


    def serve(self, t):
        self.total_elapsed_time += t

        if self.policy == "PS":
            while t > 0:
                num_jobs = self.jobs.__len__()
                extra_t = 0
                if num_jobs > 0:
                    chunk_t = t / float(num_jobs)
                for job in self.jobs:
                    extra_t += job.consume(chunk_t)
                    if job.is_done:
                        self.length -= 1
                        self.jobs[self.jobs.index(job)] = None
                while self.jobs.count(None) > 0:
                    self.jobs.pop(self.jobs.index(None))
                t = extra_t

        if self.policy == "Random" or self.policy == "SRJF" or self.policy == "FCFS":
            if self.current_servicing_job is None:
                self.choose_job_to_service()
            if self.current_servicing_job is not None:
                while t > 0:
                    extra_t = self.current_servicing_job.consume(t)
                    for job in self.jobs:
                        job.waiting_time += t - extra_t
                        self.stats.waiting_time += t - extra_t
                    if self.current_servicing_job.is_done:
                        self.current_servicing_job = None
                        self.length -= 1
                        self.choose_job_to_service()
                    if self.current_servicing_job is None:
                        break
                    t = extra_t


    def choose_job_to_service(self):

        if self.policy == "Random":
            if self.jobs.__len__() > 0:
                job = self.jobs.pop(randint(0, self.length - 1))
                self.current_servicing_job = job
            else:
                self.current_servicing_job = None

        if self.policy == "SRJF":
            min_remaining_time = float("inf")
            min_job = None
            for job in self.jobs:
                remaining_time = job.total_time_needed - job.consumed_time
                if remaining_time < min_remaining_time:
                    min_remaining_time = remaining_time
                    min_job = job
            self.current_servicing_job = min_job
            if min_job is not None:
                self.jobs.pop(self.jobs.index(min_job))

        if self.policy == "FCFS":
            if self.jobs.__len__() > 0:
                job = self.jobs.pop(0)
                self.current_servicing_job = job
            else:
                self.current_servicing_job = None


    def generate_job(self):
        return SimpleJob(generate_random_expo(self.service_time))