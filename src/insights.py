from src.jobs import read


def get_unique_job_types(path):
    read_jobs = read(path)

    job_types = set()

    for job in read_jobs:
        if job["job_type"] != '':
            job_types.add(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


def get_unique_industries(path):
    read_jobs = read(path)

    unique_industries = set()

    for job in read_jobs:
        if job["industry"] != '':
            unique_industries.add(job["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


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


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    pass


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
