def shortest_job_first(jobs):
    jobs.sort(key=lambda x: x['duration'])
    time = 0
    for job in jobs:
        time += job['duration']
        print(f"Job {job['id']} completed at time {time}")

jobs_sjf = [{'id': 1, 'duration': 6}, {'id': 2, 'duration': 2}, {'id': 3, 'duration': 4}]
shortest_job_first(jobs_sjf)