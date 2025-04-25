from collections import deque

def round_robin(jobs, quantum):
    queue = deque(jobs)
    time = 0
    while queue:
        job = queue.popleft()
        if job['remaining'] > quantum:
            time += quantum
            job['remaining'] -= quantum
            queue.append(job)
        else:
            time += job['remaining']
            job['remaining'] = 0
            print(f"Job {job['id']} completed at time {time}")

jobs_rr = [{'id': 1, 'remaining': 10}, {'id': 2, 'remaining': 4}, {'id': 3, 'remaining': 6}]
round_robin(jobs_rr, quantum=3)