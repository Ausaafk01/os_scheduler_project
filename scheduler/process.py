class Process:
    def __init__(self, pid, arrival, burst):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.remaining = burst

        # Metrics
        self.start = None
        self.completion = None
        self.waiting = 0
        self.turnaround = 0
        self.response = None

    def reset(self):
        self.remaining = self.burst
        self.start = None
        self.completion = None
        self.waiting = 0
        self.turnaround = 0
        self.response = None

    def __repr__(self):
        return f"{self.pid}(AT={self.arrival}, BT={self.burst})"