from flask import Flask, render_template, request, jsonify

from scheduler.process import Process
from scheduler.fcfs import fcfs
from scheduler.sjf import sjf
from scheduler.rr import round_robin
from scheduler.srtf import srtf
from scheduler.utils import compute_metrics, export_results, gantt_to_timeline, reset_processes

app = Flask(__name__)

# -------------------------------------
# Home Page (UI)
# -------------------------------------
@app.route('/')
def home():
    return render_template('index.html')

# -------------------------------------
# API: Run Scheduling
# -------------------------------------
@app.route('/run', methods=['POST'])
def run_scheduler():
    data = request.get_json()

    processes = []
    for item in data['processes']:
        processes.append(Process(item['pid'], int(item['arrival']), int(item['burst'])))

    quantum = int(data.get('quantum', 2))

    results = {}

    # ---------- FCFS ----------
    p1 = reset_processes([Process(p.pid, p.arrival, p.burst) for p in processes])
    g1 = fcfs(p1)
    results['FCFS'] = {
        'gantt': gantt_to_timeline(g1),
        'metrics': compute_metrics(p1, g1)
    }

    # ---------- SJF ----------
    p2 = reset_processes([Process(p.pid, p.arrival, p.burst) for p in processes])
    g2 = sjf(p2)
    results['SJF'] = {
        'gantt': gantt_to_timeline(g2),
        'metrics': compute_metrics(p2, g2)
    }

    # ---------- RR ----------
    p3 = reset_processes([Process(p.pid, p.arrival, p.burst) for p in processes])
    g3 = round_robin(p3, quantum)
    results['RR'] = {
        'gantt': gantt_to_timeline(g3),
        'metrics': compute_metrics(p3, g3)
    }

    # ---------- SRTF ----------
    p4 = reset_processes([Process(p.pid, p.arrival, p.burst) for p in processes])
    g4 = srtf(p4)
    results['SRTF'] = {
        'gantt': gantt_to_timeline(g4),
        'metrics': compute_metrics(p4, g4)
    }

    # Optional export
    if data.get('export'):
        export_results(p4)

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)