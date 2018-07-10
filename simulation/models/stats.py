class StatsAggregator():

    total_done_jobs = 0
    total_time = 0

    def __init__(self, capacity):
        self.blocked_jobs = 0
        self.num_incoming_jobs = 0

        self.length = 0
        self.num_length_reports = 0

        self.waiting_time = 0
        self.num_enqueue_jobs = 0

        self.capacity = capacity


    def aggregate_results(self):
        avg_blocked_jobs = self.blocked_jobs / float(self.num_incoming_jobs)
        avg_length = self.length / float(self.num_length_reports)
        avg_waiting_time = self.waiting_time / float(self.num_enqueue_jobs)
        return avg_blocked_jobs, avg_length, avg_waiting_time
