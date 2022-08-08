def filter_by_job_type(jobs, job_type):
    jobs_by_type = []

    for job in jobs:
        if (job_type != '' and job["job_type"] == job_type):
            jobs_by_type.append(job)

    return jobs_by_type
