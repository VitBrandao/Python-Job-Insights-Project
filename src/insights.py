from src.jobs import read


def get_unique_job_types(path):
    read_jobs = read(path)

    job_types = set()

    for job in read_jobs:
        if job["job_type"] != '':
            job_types.add(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    jobs_by_type = []

    for job in jobs:
        if (job_type != '' and job["job_type"] == job_type):
            jobs_by_type.append(job)

    return jobs_by_type


def get_unique_industries(path):
    read_jobs = read(path)

    unique_industries = set()

    for job in read_jobs:
        if job["industry"] != '':
            unique_industries.add(job["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    jobs_by_industry = []

    for job in jobs:
        if (industry != '' and job["industry"] == industry):
            jobs_by_industry.append(job)

    return jobs_by_industry


def create_max_salaries_list(file):
    all_max_salaries = set()
    for job in file:
        if job["max_salary"] != '':
            all_max_salaries.add(job["max_salary"])
    return all_max_salaries


def get_max_salary(path):
    read_jobs = read(path)

    all_max_salaries = create_max_salaries_list(read_jobs)

    higher_max_salary = 0

    for salary in all_max_salaries:
        # https://www.programiz.com/python-programming/methods/string/isnumeric
        if salary.isnumeric():
            salary = int(salary)
            if salary > higher_max_salary:
                higher_max_salary = salary
    return higher_max_salary


def create_min_salaries_list(file):
    all_min_salaries = set()
    for job in file:
        if job["min_salary"] != '':
            all_min_salaries.add(job["min_salary"])
    return all_min_salaries


def get_min_salary(path):
    read_jobs = read(path)

    all_min_salaries = create_min_salaries_list(read_jobs)

    lower_min_salary = 1000000

    for salary in all_min_salaries:
        if salary.isnumeric():
            salary = int(salary)
            if salary < lower_min_salary:
                lower_min_salary = salary
    return lower_min_salary


def matches_salary_range(job, salary):
    # https://stackoverflow.com/questions/10406130/check-if-something-is-not-in-a-list-in-python
    if("min_salary" not in job or "max_salary" not in job):
        raise ValueError

    elif(
        type(job["min_salary"]) != int or
        type(job["min_salary"]) != int
    ):
        raise ValueError

    elif(job["min_salary"] > job["max_salary"]):
        raise ValueError

    elif(type(salary) != int):
        raise ValueError

    is_salary_in_range = (job["min_salary"] <= salary <= job["max_salary"])
    return is_salary_in_range  # retorna booleano a partir da condição acima


def filter_by_salary_range(jobs, salary):
    jobs_that_match_salary = []

    for job in jobs:
        try:
            if (matches_salary_range(job, salary)):
                jobs_that_match_salary.append(job)
        except ValueError:
            print(f"An error occured with the following value: {job}")

    return jobs_that_match_salary
