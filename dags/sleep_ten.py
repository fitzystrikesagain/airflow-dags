from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator

from datetime import datetime, timedelta

default_args = {
    "start_date": datetime(2022, 10, 13),
    "owner": "Airflow",
}

with DAG(dag_id="sleep_ten_seconds",
         schedule_interval="@hourly",
         default_args=default_args,
         dagrun_timeout=timedelta(hours=1),
         description="sleeps for 10s",
         catchup=False) as dag:
    dag.doc_md = "# Sleep, child"
    # Tasks dynamically generated
    start = DummyOperator(task_id="start")
    tasks = [BashOperator(
        task_id=f"task_{t}",
        bash_command="sleep 10") for t in range(1, 4)]

    all_done = DummyOperator(task_id="all_done")
    start >> tasks >> all_done
