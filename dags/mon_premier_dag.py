import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

def start_pipeline():
    print("Start of the Big Data pipeline")

def process_pipeline():
    print("Processing in progress")
    print("Simulating a data processing step")

def end_pipeline():
    print("End of the Big Data pipeline")

with DAG(
    dag_id="mon_premier_dag",
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    schedule=None,  
    catchup=False,
    tags=["initiation", "python-operator"],
) as dag:

    start_task = PythonOperator(
        task_id="debut",
        python_callable=start_pipeline,
    )

    process_task = PythonOperator(
        task_id="traitement",
        python_callable=process_pipeline,
    )

    end_task = PythonOperator(
        task_id="fin",
        python_callable=end_pipeline,
    )

    start_task >> process_task >> end_task