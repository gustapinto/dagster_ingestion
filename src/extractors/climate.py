from dagster import op
from requests import get


'''
A OP is the basic building block of a dagster workflow, creating and
running a task, they can be connected to create a graph of tasks
'''
@op
def extract_climate_data() -> list:
    endpoint = 'https://cptecextractor.gustapinto.dev/api/export/kind=tempmax'

    json_list = get(endpoint).json()

    return json_list
