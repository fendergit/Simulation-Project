from utils.functions import generate_random_expo

class SimpleJob():


    def __init__(self, total):
        self.total_time_needed = total
        self.consumed_time = 0
        self.waiting_time = 0
        self.system_time = 0
        self.is_done = False
        self.is_blocked = False
        self.next_queue = None
        self.current_queue = None


    def __str__(self):
        return "total " + str(self.total_time_needed) + " " + \
               "consumed " + str(self.consumed_time) + " " + \
               "waiting " + str(self.waiting_time) + " " + \
               "done " + str(self.is_done) + " " + \
               "blocked " + str(self.is_blocked)


    def make_done(self, extra_t):
        self.is_done = True
        if self.current_queue.policy == "PS" or self.current_queue.policy == "FCFS":
            self.current_queue.stats.total_done_jobs += 1
        if self.next_queue is not None:
            self.total_time_needed += generate_random_expo(self.next_queue.service_time)
            self.next_queue.done_jobs.append((self, extra_t))


    def consume(self, t):
        if self.consumed_time + t < self.total_time_needed:
            self.consumed_time += t
            extra = 0
        else:
            extra = self.consumed_time + t - self.total_time_needed
            self.consumed_time = self.total_time_needed
            self.make_done(extra)
        return extra


