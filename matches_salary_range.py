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
