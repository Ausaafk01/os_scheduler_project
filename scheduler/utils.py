import csv


def compute_metrics(processes, gantt):
    """Return average WT, TAT, RT and CPU utilization."""
    total_time = gantt[-1][2] if gantt else 0
    busy_time = sum(end - start for pid, start, end in gantt if pid != "IDLE")

    cpu_util = (busy_time / total_time) * 100 if total_time else 0

    avg_wt = sum(p.waiting for p in processes) / len(processes)
    avg_tat = sum(p.turnaround for p in processes) / len(processes)
    avg_rt = sum((p.response if p.response is not None else 0) for p in processes) / len(processes)

    return {
        "avg_wt": round(avg_wt, 2),
        "avg_tat": round(avg_tat, 2),
        "avg_rt": round(avg_rt, 2),
        "cpu_util": round(cpu_util, 2),
    }


def export_results(processes, filename="data/results.csv"):
    """Export process metrics to CSV."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["PID", "AT", "BT", "WT", "TAT", "RT"])
        for p in processes:
            writer.writerow([p.pid, p.arrival, p.burst, p.waiting, p.turnaround, p.response])

    return filename


def gantt_to_timeline(gantt):
    """Convert gantt list to structured timeline for frontend."""
    timeline = []
    for pid, start, end in gantt:
        timeline.append({
            "pid": pid,
            "start": start,
            "end": end,
            "duration": end - start
        })
    return timeline


def reset_processes(processes):
    """Reset all process metrics for reuse across algorithms."""
    for p in processes:
        p.reset()
    return processes