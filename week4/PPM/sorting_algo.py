import heapq
from collections import deque
import matplotlib.pyplot as plt

# Define a Job class to store job attributes
class Job:
    def __init__(self, name, arrival_time, burst_time, deadline=None):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.deadline = deadline
        self.finish_time = 0

# Round Robin Scheduling Algorithm
def round_robin(jobs, time_quantum):
    time = 0
    queue = deque(sorted(jobs, key=lambda x: x.arrival_time))
    completed_jobs = []
    timeline = []

    while queue:
        job = queue.popleft()
        if job.arrival_time > time:
            time = job.arrival_time
        exec_time = min(time_quantum, job.remaining_time)
        job.remaining_time -= exec_time
        time += exec_time
        timeline.append((job.name, time))

        if job.remaining_time > 0:
            queue.append(job)
        else:
            job.finish_time = time
            completed_jobs.append(job)

    return timeline

# Earliest Deadline First Scheduling Algorithm
def edf(jobs):
    time = 0
    timeline = []
    queue = sorted(jobs, key=lambda x: (x.arrival_time, x.deadline))
    ready_queue = []

    while queue or ready_queue:
        while queue and queue[0].arrival_time <= time:
            heapq.heappush(ready_queue, (queue[0].deadline, queue.pop(0)))

        if ready_queue:
            _, job = heapq.heappop(ready_queue)
            time += job.burst_time
            job.finish_time = time
            timeline.append((job.name, time))
        else:
            time += 1

    return timeline

# Shortest Job First (Greedy) Scheduling Algorithm
def sjf(jobs):
    time = 0
    timeline = []
    queue = sorted(jobs, key=lambda x: x.arrival_time)
    ready_queue = []

    while queue or ready_queue:
        while queue and queue[0].arrival_time <= time:
            heapq.heappush(ready_queue, (queue[0].burst_time, queue.pop(0)))

        if ready_queue:
            _, job = heapq.heappop(ready_queue)
            time += job.burst_time
            job.finish_time = time
            timeline.append((job.name, time))
        else:
            time += 1

    return timeline

# Generate a list of sample jobs
def generate_test_jobs():
    return [
        Job("Job1", 0, 4, deadline=8),
        Job("Job2", 1, 3, deadline=6),
        Job("Job3", 2, 2, deadline=9),
        Job("Job4", 3, 1, deadline=10)
    ]

# Save the job execution timeline as an image
def visualize_timeline(timeline, title, filename):
    fig, ax = plt.subplots()
    start = 0
    for job_name, end in timeline:
        ax.broken_barh([(start, end - start)], (10, 9), facecolors='tab:blue')
        ax.text(start + (end - start) / 2, 14, job_name, ha='center')
        start = end
    ax.set_ylim(5, 35)
    ax.set_xlim(0, start + 1)
    ax.set_xlabel('Time')
    ax.set_yticks([])
    ax.set_title(title)
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

# Run and visualize each scheduling algorithm
jobs_rr = generate_test_jobs()
jobs_edf = generate_test_jobs()
jobs_sjf = generate_test_jobs()

timeline_rr = round_robin(jobs_rr, time_quantum=2)
timeline_edf = edf(jobs_edf)
timeline_sjf = sjf(jobs_sjf)

visualize_timeline(timeline_rr, "Round Robin Scheduling", "round_robin.png")
visualize_timeline(timeline_edf, "Earliest Deadline First Scheduling", "edf.png")
visualize_timeline(timeline_sjf, "Shortest Job First (Greedy) Scheduling", "sjf.png")