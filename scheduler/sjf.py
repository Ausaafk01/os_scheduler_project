from .process import Process


def sjf(processes):
    time = 0
    completed = 0
    n = len(processes)
    gantt = []
    done = [False] * n

    while completed < n:
        # Get all arrived and not completed processes
        available = [(i, p) for i, p in enumerate(processes) if p.arrival <= time and not done[i]]

        if not available:
            # CPU idle until next arrival
            next_arrival = min(p.arrival for i, p in enumerate(processes) if not done[i])
            gantt.append(("IDLE", time, next_arrival))
            time = next_arrival
            continue

        # Pick shortest job
        idx, proc = min(available, key=lambda x: x[1].burst)

        if proc.response is None:
            proc.response = time - proc.arrival

        proc.start = time
        time += proc.burst
        proc.completion = time
        proc.turnaround = proc.completion - proc.arrival
        proc.waiting = proc.turnaround - proc.burst

        gantt.append((proc.pid, proc.start, proc.completion))

        done[idx] = True
        completed += 1

    return gantt