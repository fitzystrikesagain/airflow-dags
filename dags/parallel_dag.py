from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2019, 1, 1),
    'owner': 'Airflow',
}


def process(p1):
    print(p1)
    return 'done'


with DAG(dag_id='parallel_dag',
         schedule_interval='0 0 * * *',
         description="Parallel task execution",
         default_args=default_args,
         dagrun_timeout=timedelta(hours=1),
         on_failure_callback=lambda x: print(x),
         catchup=False) as dag:
    dag.doc_md = """# Parallel DAG"""
    # Tasks dynamically generated
    tasks = [BashOperator(task_id='task_{0}'.format(t), bash_command='sleep 60'.format(t)) for t in range(1, 4)]

    task_4 = PythonOperator(task_id='task_4', python_callable=process, op_args=['my super parameter'])

    task_5 = BashOperator(task_id='task_5', bash_command='echo "pipeline done"')

    task_6 = BashOperator(task_id='task_6', bash_command='sleep 60')

    tasks >> task_4 >> task_5 >> task_6
