# CPU Scheduling Simulator (Web-Based)

A web-based CPU scheduling simulator that visualizes and compares common scheduling algorithms with a clean UI, Gantt chart output, and CPU utilization metrics.

---

## 🚀 Features

* Supports multiple CPU scheduling algorithms:

  * First Come First Serve (FCFS)
  * Shortest Job First (SJF – Non-Preemptive)
  * Round Robin (RR)
  * Shortest Remaining Time First (SRTF – Preemptive)
* Interactive web UI to input processes
* Visual Gantt charts for each algorithm
* CPU utilization graph
* Performance metrics:

  * Average Waiting Time
  * Average Turnaround Time
  * Average Response Time
  * CPU Utilization %
* Optional CSV export of results

---

## 📁 Project Structure

```
project_os/
│
├── app.py                  # Flask backend entry point
├── requirements.txt        # Python dependencies
│
├── scheduler/              # Scheduling algorithms and utilities
│   ├── __init__.py
│   ├── process.py          # Process class definition
│   ├── fcfs.py             # FCFS implementation
│   ├── sjf.py              # SJF implementation
│   ├── rr.py               # Round Robin implementation
│   ├── srtf.py             # SRTF implementation
│   └── utils.py            # Helpers (metrics, export, formatting)
│
├── templates/
│   └── index.html          # Web UI
│
├── static/                 # Optional static files
│
└── data/                   # Exported results (optional)
```

---

## 🛠️ Installation & Setup

### 1. Clone or Download the Project

Ensure your project is located in:

```
E:\project_os
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

* Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

---

### 3. Install Dependencies

```bash
pip install flask
```

Or:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Flask server:

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🧪 How to Use

1. Enter the number of processes.
2. Click **Create** to generate input fields.
3. Enter:

   * Process ID
   * Arrival Time
   * Burst Time
4. Set a time quantum (used by Round Robin).
5. Click **Run Simulation**.

The page will display:

* CPU utilization chart
* Gantt charts for each algorithm
* Performance metrics

---

## 📊 Metrics Explained

* **Waiting Time (WT):** Time spent waiting in the ready queue.
* **Turnaround Time (TAT):** Completion time minus arrival time.
* **Response Time (RT):** Time from arrival to first execution.
* **CPU Utilization:** Percentage of time the CPU was actively executing processes.

---

## 📤 Optional CSV Export

Check the **Export CSV** box before running the simulation to export results to:

```
data/results.csv
```

---

## 📌 Notes

* This is a development version; do not use Flask’s built-in server for production.
* Ensure all process fields are filled correctly to avoid errors.

---

## 📄 License

This project is provided for educational purposes.
