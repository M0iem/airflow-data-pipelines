import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

def receive_dossiers():
    print("Step 1: Receiving student enrollment dossiers")

def store_in_data_lake():
    print("Step 2: Storing raw files inside the Data Lake zone")

def validate_compliance():
    print("Step 3: Checking compliance and validity of received files")

def clean_data_records():
    print("Step 4: Cleaning data (removing duplicates, format corrections)")

def assign_departments():
    print("Step 5 (Parallel A): Automatically assigning students based on their branch choice")

def calculate_stats():
    print("Step 5 (Parallel B): Calculating statistical analysis of candidates per specialty")

def compile_final_report():
    print("Step 6: Generating the final unified student registration report")

with DAG(
    dag_id="pipeline_big_data_parallele",
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=["big-data", "parallel", "python-operator"],
) as dag:

    task_reception = PythonOperator(task_id="reception", python_callable=receive_dossiers)
    task_stockage = PythonOperator(task_id="stockage", python_callable=store_in_data_lake)
    task_validation = PythonOperator(task_id="validation", python_callable=validate_compliance)
    task_nettoyage = PythonOperator(task_id="nettoyage", python_callable=clean_data_records)
    
    task_affectation = PythonOperator(task_id="affectation", python_callable=assign_departments)
    task_statistiques = PythonOperator(task_id="generation_statistiques", python_callable=calculate_stats)
    
    task_rapport = PythonOperator(task_id="rapport_final", python_callable=compile_final_report)

    task_reception >> task_stockage >> task_validation >> task_nettoyage
    task_nettoyage >> [task_affectation, task_statistiques]
    [task_affectation, task_statistiques] >> task_rapport