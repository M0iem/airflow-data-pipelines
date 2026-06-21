# 🚀 Big Data Pipeline Orchestration with Apache Airflow

## 📌 Overview
This repository contains a complete, containerized Apache Airflow environment demonstrating the orchestration of Big Data pipelines. It showcases Extract, Transform, Load (ETL) processes, strict sequential task dependencies, and advanced parallel execution workflows using Python.

## 📂 Project Structure (DAGs)

The project features three main data pipelines located in the `dags/` directory:

### 1. `mon_premier_dag.py` (Basic Linear Pipeline)
A foundational Directed Acyclic Graph (DAG) to test the Airflow environment and verify that tasks execute in a strict sequential order.
* **Flow:** Start Pipeline ➔ Process Data ➔ End Pipeline

### 2. `pipeline_big_data_python.py` (Sequential ETL Pipeline)
A complete ETL pipeline simulating the processing of raw sales data. 
* **Workflow:** 1. **Ingestion:** Generates raw sales data (CSV).
  2. **Storage:** Simulates landing the data in a Data Lake.
  3. **Validation:** Checks the data schema and column integrity.
  4. **Transformation:** Cleans the data and calculates total transaction amounts.
  5. **Analytics:** Aggregates total revenue per city.
  6. **Loading:** Simulates pushing the cleaned data to a Data Warehouse.
  7. **Reporting:** Generates a final readable text report.

### 3. `pipeline_big_data_parallele.py` (Parallel Processing Pipeline)
An advanced pipeline simulating a student university enrollment system. It demonstrates how Airflow handles branching and simultaneous execution to optimize processing time for large datasets.
* **Workflow:** Receives Files ➔ Stores ➔ Validates ➔ Cleans ➔ **[Parallel Execution: Assigns Departments AND Calculates Statistics simultaneously]** ➔ Compiles Final Unified Report.

## 🛠️ Technologies Used
* **Apache Airflow:** For pipeline orchestration, monitoring, and scheduling.
* **Python:** Core language for writing DAGs and data processing scripts (`PythonOperator`).
* **Docker & Docker Compose:** For containerizing the Airflow webserver, scheduler, and PostgreSQL database for isolated execution.
* **PostgreSQL:** Metadata database for Airflow state management.

## 🚀 Getting Started

### Prerequisites
Make sure you have [Docker](https://www.docker.com/) and Docker Compose installed on your local machine.

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/AnaasIH/airflow-data-pipelines.git](https://github.com/AnaasIH/airflow-data-pipelines.git)
   cd airflow-data-pipelines


Start the Airflow environment:
docker compose up -d

Initialize the Database & User (If running for the first time):
docker compose run airflow-webserver airflow db init
docker compose run airflow-webserver airflow users create --username airflow --password airflow --firstname Admin --lastname Admin --role Admin --email admin@example.com

Access the Airflow Web Interface:
Open your browser and navigate to: http://localhost:8080
Username: airflow
Password: airflow

Execute the DAGs:
Unpause the DAGs using the toggle button in the UI.
Click the "Trigger DAG" (play) button to start the pipelines.
Open the Graph View to watch the data flow execute in real-time!

🛑 Stopping the Environment
To safely shut down the containers:
docker compose down
