from dagster import job

from src.extractors.climate import extract_climate_data
from src.loaders.climate import load_climate_data

'''
For dagster a job is just a aggregation of operations (OP), so most
dagster jobs are just wrappers for operations to be orquestrated
'''
@job
def ingest_climate_data() -> None:
    load_climate_data(extract_climate_data())
