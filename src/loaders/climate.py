from csv import QUOTE_MINIMAL, writer
from os.path import isfile

from dagster import op


'''
A OP is the basic building block of a dagster workflow, creating and
running a task, they can be connected to create a graph of tasks
'''
@op
def load_climate_data(data: list) -> None:
    headers = ['year', 'january', 'february', 'march', 'april', 'may',
               'june', 'july', 'august', 'september', 'october',
               'november', 'december']
    rows = [d.values() for d in data]

    with open('climate.csv', 'w') as csvfile:
        csvwriter = writer(csvfile, delimiter='|')

        csvwriter.writerow(headers)
        csvwriter.writerows(rows)
