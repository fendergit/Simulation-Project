class SimpleJob():

    total_time_needed = 1.00
    consumed_time = 0
    waiting_time = 0
    system_time = 0
    # server_time = 0
    is_done = False


    def __init__(self, total):
        self.total_time_needed = total


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


