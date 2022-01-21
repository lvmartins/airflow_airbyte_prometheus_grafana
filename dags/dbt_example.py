
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.version import version
from datetime import datetime, timedelta
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.utils.dates import days_ago
#from airflow_dbt_python.operators.dbt import (
#   DbtSeedOperator,
#   DbtSnapshotOperator,
#   DbtRunOperator,
#   DbtTestOperator
#)

#
# The default dir contains my dbt models, the retries has been added
# to handle if the cloud provider is offline for maintenance (this happened).
# Finally, I allow 30 minutes to attempt a re-execution of the DAG
#

#default_args = {
   # 'dir': '/home/dev/dbt',
   # 'start_date': days_ago(0),
   # 'retries': 1,
   # 'retry_delay': timedelta(minutes=30)
#}

DBT_PROJECT_DIR = '/home/dev/dbt'
DBT_PROFILE_DIR = '/home/fcoelho/.dbt'

with DAG('example_dag_2',

         start_date=datetime(2019, 1, 1)) as dag:
	dbt_run = BashOperator(
	task_id="dbt_run",
#	bash_command=f"dbt run --profiles-dir {DBT_PROFILE_DIR} --project-dir {DBT_PROJECT_DIR}"
	bash_command='pwd'
)





