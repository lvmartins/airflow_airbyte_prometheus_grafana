from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.version import version
from datetime import datetime, timedelta
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.utils.dates import days_ago

# Using a DAG context manager, you don't have to specify the dag property of each task
with DAG('example_dag',
         default_args={'owner': 'airflow'},
         schedule_interval='@daily',
         start_date=days_ago(1)
         # catchup=False # enable if you don't want historical dag runs to run
         ) as dag:

     t0 = DummyOperator(
          task_id='dummy',
     )
     t1 = AirbyteTriggerSyncOperator(
         task_id='airbyte_trigger',
         airbyte_conn_id='airbyte_conn_example',
         connection_id='83b5e2f3-a1ae-42ac-ae52-c086cf13204e',
         asynchronous=False,
         timeout=3600,
         wait_seconds=10
     )

     t2 = BashOperator (
   	 task_id= 'dbt_trigger',
	 bash_command = 'pwd'
     )

     t0 >> t1 >> t2 # indented inside for loop so each task is added downstream of t0
