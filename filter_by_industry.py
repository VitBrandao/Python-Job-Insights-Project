def filter_by_industry(jobs, industry):
    jobs_by_industry = []

    for job in jobs:
        if (industry != '' and job["industry"] == industry):
            jobs_by_industry.append(job)

    return jobs_by_industry

