def earliest_deadline_first(jobs):
    jobs.sort(key=lambda x: x['deadline'])
    time = 0
    for job in jobs:
        time += job['duration']
        print(f"Job {job['id']} completed at time {time} (Deadline: {job['deadline']})")

jobs_edf = [{'id': 1, 'duration': 4, 'deadline': 10}, {'id': 2, 'duration': 2, 'deadline': 5}, {'id': 3, 'duration': 3, 'deadline': 8}]
earliest_deadline_first(jobs_edf)