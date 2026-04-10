from .process import Process


def round_robin(processes, quantum):
    # Sort by arrival time
    processes.sort(key=lambda p: p.arrival)

    time = 0
    queue = []
    gantt = []
    completed = 0
    n = len(processes)
    i = 0  # arrival index

    while completed < n:
        # Add newly arrived processes to queue
        while i < n and processes[i].arrival <= time:
            queue.append(processes[i])
            i += 1

        # If no process ready, CPU idle
        if not queue:
            next_time = processes[i].arrival
            gantt.append(("IDLE", time, next_time))
            time = next_time
            continue

        current = queue.pop(0)

        # Set response time
        if current.response is None:
            current.response = time - current.arrival

        run_time = min(quantum, current.remaining)
        gantt.append((current.pid, time, time + run_time))
        time += run_time
        current.remaining -= run_time

        # Add new arrivals during this slice
        while i < n and processes[i].arrival <= time:
            queue.append(processes[i])
            i += 1

        # If not finished, put back in queue
        if current.remaining > 0:
            queue.append(current)
        else:
            current.completion = time
            current.turnaround = current.completion - current.arrival
            current.waiting = current.turnaround - current.burst
            completed += 1

    return gantt