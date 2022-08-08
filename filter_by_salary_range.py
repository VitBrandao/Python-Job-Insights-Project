from insights import matches_salary_range

def filter_by_salary_range(jobs, salary):
    jobs_that_match_salary = []

    for job in jobs:
        try:
            if (matches_salary_range(job, salary)):
                jobs_that_match_salary.append(job)
        except ValueError:
            print(f"An error occured with the following value: {job}")

    return jobs_that_match_salary
