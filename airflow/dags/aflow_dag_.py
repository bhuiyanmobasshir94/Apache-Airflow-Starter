from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


def add(a=1, b=2):
    return a+b


def sub(a=5, b=2):
    return a-b


default_args = {
    "owner": "airflow",
}

with DAG(
    dag_id="aflow_dag",
    description="Datalake to datawarehouse creation",
    default_args=default_args,
    schedule_interval="@daily",
    schedule_interval=None,
    start_date=days_ago(2),
    tags=["aflow", "dwh", "datalake", "etl/elt"],
) as dag:
    add = PythonOperator(
        task_id="add", python_callable=add,
    )
    sub = PythonOperator(
        task_id="sub", python_callable=sub,
    )

add >> sub
