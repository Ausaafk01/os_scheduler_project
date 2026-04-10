from .process import Process


def srtf(processes):
    time = 0
    completed = 0
    n = len(processes)
    gantt = []

    current_pid = None
    start_time = None

    while completed < n:
        available = [p for p in processes if p.arrival <= time and p.remaining > 0]

        if not available:
            time += 1
            continue

        current = min(available, key=lambda p: p.remaining)

        if current_pid != current.pid:
            if current_pid is not None:
                gantt.append((current_pid, start_time, time))
            current_pid = current.pid
            start_time = time

        if current.response is None:
            current.response = time - current.arrival

        current.remaining -= 1
        time += 1

        if current.remaining == 0:
            current.completion = time
            current.turnaround = current.completion - current.arrival
            current.waiting = current.turnaround - current.burst
            completed += 1

    if current_pid is not None:
        gantt.append((current_pid, start_time, time))

    return gantt