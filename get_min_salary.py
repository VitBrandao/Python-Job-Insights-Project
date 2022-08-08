from jobs import read


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
