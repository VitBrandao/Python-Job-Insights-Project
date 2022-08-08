from jobs import read

def get_unique_industries(path):
    read_jobs = read(path)

    unique_industries = set()

    for job in read_jobs:
        if job["industry"] != '':
            unique_industries.add(job["industry"])
    return unique_industries
