from jobs import read

def get_unique_job_types(path):
    read_jobs = read(path)

    job_types = set()

    for job in read_jobs:
        if job["job_type"] != '':
            job_types.add(job["job_type"])

    return job_types
