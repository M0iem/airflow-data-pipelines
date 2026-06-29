Hna README kamel **ready copier/coller**:

```markdown
# 🚀 Airflow Data Pipelines

## 📋 Description

This project implements automated data pipelines using **Apache Airflow**, **Docker**, and **Docker Compose**.

The goal is to create, manage, and execute data workflows using Airflow DAGs in a containerized environment.

---

# 🛠️ Technologies Used

- Apache Airflow
- Docker
- Docker Compose
- Python
- Data Engineering
- Workflow Automation
- DAG Scheduling

---

# 📂 Project Structure

```

airflow-data-pipelines/
│
├── dags/
│   └── Airflow DAG files
│
├── docker-compose.yml
│
├── README.md
│
└── Other configuration files

````

---

# ✅ Prerequisites

Before starting, make sure you have installed:

- Docker
- Docker Compose
- Git

Check installation:

```bash
docker --version
docker compose version
git --version
````

---

# ⚙️ Installation & Setup

## 1. Clone the repository

```bash
git clone https://github.com/M0iem/airflow-data-pipelines.git
```

Go inside the project:

```bash
cd airflow-data-pipelines
```

---

# ▶️ Start Airflow Environment

Run Docker Compose:

```bash
docker compose up -d
```

This will start all required Airflow services.

---

# 🗄️ Initialize Airflow Database

Initialize the database:

```bash
docker compose run airflow-webserver airflow db init
```

Create an Airflow user:

```bash
docker compose run airflow-webserver airflow users create \
--username airflow \
--password airflow \
--firstname Admin \
--lastname Admin \
--role Admin \
--email admin@example.com
```

---

# 🌐 Access Airflow Web Interface

Open your browser:

```
http://localhost:8080
```

Login credentials:

```
Username: airflow

Password: airflow
```

---

# ▶️ Execute DAG Pipelines

From the Airflow Web Interface:

1. Enable the DAGs
2. Click on **Trigger DAG**
3. Open **Graph View**
4. Monitor the pipeline execution

---

# 🛑 Stop Airflow Environment

To stop all containers:

```bash
docker compose down
```

---

# 🔄 Restart Environment

Start again:

```bash
docker compose up -d
```

---

# 📌 Notes

* All pipelines are managed through Airflow DAGs.
* Docker ensures a reproducible execution environment.
* Airflow UI allows monitoring and scheduling workflows.

---

# 👤 Author

Meriem Yafir

