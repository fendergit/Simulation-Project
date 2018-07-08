class SimpleJob():

    total_time_needed = 1.00
    consumed_time = 0
    waiting_time = 0
    system_time = 0
    # server_time = 0
    is_done = False
    is_blocked = False


    def __init__(self, total):
        self.total_time_needed = total


    def __str__(self):
        return "total " + str(self.total_time_needed) + " " + \
               "consumed " + str(self.consumed_time) + " " + \
               "waiting " + str(self.waiting_time) + " " + \
               "done " + str(self.is_done) + " " + \
               "blocked " + str(self.is_blocked) + "\n"


    def can_be_done(self, t):
        if self.consumed_time + t >= self.total_time_needed:
            return True
        return False


    def consume(self, t):
        if self.consumed_time + t < self.total_time_needed:
            self.consumed_time += t
            extra = 0
        else:
            extra = self.consumed_time + t - self.total_time_needed
            self.consumed_time = self.total_time_needed
            self.is_done = True
        return extra


