from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as jobs:
        jobs_reader = list(csv.DictReader(jobs))

    return jobs_reader
