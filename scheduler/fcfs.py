from .process import Process


def fcfs(processes):
    # Sort by arrival time
    processes.sort(key=lambda p: p.arrival)

    time = 0
    gantt = []

    for p in processes:
        # Idle CPU
        if time < p.arrival:
            gantt.append(("IDLE", time, p.arrival))
            time = p.arrival

        if p.response is None:
            p.response = time - p.arrival

        p.start = time
        time += p.burst
        p.completion = time
        p.turnaround = p.completion - p.arrival
        p.waiting = p.turnaround - p.burst

        gantt.append((p.pid, p.start, p.completion))

    return gantt