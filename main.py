from src.jobs.climate import ingest_climate_data


"""
Dagster is a data pipeline orquestrator that treat data on a more functional
fashion, usign either CLI based executions or a web interface in the form
of Dagit
"""
if __name__ == '__main__':
    result = ingest_climate_data.execute_in_process()

    print(f'Job status: {result.success}')
