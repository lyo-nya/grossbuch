#!python3

import csv
from os import path
from sys import argv

from grossbuch.db import session
from grossbuch.models import PriceTag


def fill_db(filename):
    if not path.isfile(filename):
        return 1
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            new_job = PriceTag(job_type=row[0],
                               title=row[1],
                               unit=row[2],
                               price=row[3])
            session.add(new_job)
    session.commit()
    session.remove()
    return 0

if __name__ == "__main__":
    fill_db(argv[1])
