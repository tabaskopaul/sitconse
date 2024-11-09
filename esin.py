import os

def is_running_in_databricks() -> bool:
    return 'DATABRICKS_RUNTIME' in os.environ
