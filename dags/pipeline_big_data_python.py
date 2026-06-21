import csv
import json
import os
import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator

DATA_DIR = "/opt/airflow/data"
RAW_FILE = f"{DATA_DIR}/ventes_raw.csv"
CLEAN_FILE = f"{DATA_DIR}/ventes_clean.csv"
RESULT_FILE = f"{DATA_DIR}/resultats_ventes.json"
REPORT_FILE = f"{DATA_DIR}/rapport_pipeline.txt"

def ingest_data():
    os.makedirs(DATA_DIR, exist_ok=True)
    sales_data = [
        ["id_vente", "ville", "produit", "prix", "quantite"],
        [1, "Casablanca", "PC", 8000, 2],
        [2, "Rabat", "Clavier", 300, 5],
        [3, "Marrakech", "Souris", 150, 10],
        [4, "Casablanca", "Ecran", 2500, 3],
        [5, "Tanger", "PC", 8500, 1],
        [6, "Rabat", "Ecran", 2300, 2],
    ]
    with open(RAW_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(sales_data)
    print(f"Ingestion completed. Raw file created at: {RAW_FILE}")

def store_raw_zone():
    if not os.path.exists(RAW_FILE):
        raise FileNotFoundError("Raw file not found.")
    file_size = os.path.getsize(RAW_FILE)
    print("Storage in raw zone completed.")
    print(f"Raw file path: {RAW_FILE}")
    print(f"File size: {file_size} bytes")

def validate_data():
    if not os.path.exists(RAW_FILE):
        raise FileNotFoundError("Data file missing.")
    with open(RAW_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
    expected_columns = ["id_vente", "ville", "produit", "prix", "quantite"]
    if header != expected_columns:
        raise ValueError("Incorrect file schema validation failed.")
    print("Validation successful.")
    print(f"Detected columns: {header}")

def transform_data():
    cleaned_rows = []
    with open(RAW_FILE, mode="r", encoding="utf-8") as input_file:
        reader = csv.DictReader(input_file)
        for row in reader:
            prix = float(row["prix"])
            quantite = int(row["quantite"])
            montant = prix * quantite
            cleaned_rows.append({
                "id_vente": row["id_vente"],
                "ville": row["ville"],
                "produit": row["produit"],
                "prix": prix,
                "quantite": quantite,
                "montant": montant
            })
    with open(CLEAN_FILE, mode="w", newline="", encoding="utf-8") as output_file:
        fieldnames = ["id_vente", "ville", "produit", "prix", "quantite", "montant"]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)
    print("Data transformation completed successfully.")

def analytical_processing():
    revenue_per_city = {}
    with open(CLEAN_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            city = row["ville"]
            amount = float(row["montant"])
            revenue_per_city[city] = revenue_per_city.get(city, 0) + amount
    with open(RESULT_FILE, mode="w", encoding="utf-8") as file:
        json.dump(revenue_per_city, file, indent=4, ensure_ascii=False)
    print("Analytical processing completed.")
    print(revenue_per_city)

def load_results():
    if not os.path.exists(RESULT_FILE):
        raise FileNotFoundError("Analytical results file missing.")
    print("Loading results to Data Warehouse completed successfully.")

def generate_report():
    with open(RESULT_FILE, mode="r", encoding="utf-8") as file:
        results = json.load(file)
    with open(REPORT_FILE, mode="w", encoding="utf-8") as report:
        report.write("Big Data Pipeline Execution Report\n")
        report.write("==================================\n\n")
        for city, revenue in results.items():
            report.write(f"{city} : {revenue} DH\n")
    print("Final execution report generated.")

with DAG(
    dag_id="pipeline_big_data_python",
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=["big-data", "python-operator", "pipeline"],
) as dag:

    ingestion = PythonOperator(task_id="ingestion_donnees", python_callable=ingest_data)
    stockage = PythonOperator(task_id="stockage_zone_brute", python_callable=store_raw_zone)
    validation = PythonOperator(task_id="validation_donnees", python_callable=validate_data)
    transformation = PythonOperator(task_id="transformation_donnees", python_callable=transform_data)
    traitement = PythonOperator(task_id="traitement_analytique", python_callable=analytical_processing)
    chargement = PythonOperator(task_id="chargement_resultats", python_callable=load_results)
    rapport = PythonOperator(task_id="generation_rapport", python_callable=generate_report)

    ingestion >> stockage >> validation >> transformation >> traitement >> chargement >> rapport