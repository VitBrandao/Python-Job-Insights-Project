from jobs import read


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
