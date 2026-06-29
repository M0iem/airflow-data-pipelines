# 🚀 Airflow Data Pipelines

A professional **Data Engineering project** that demonstrates the creation, orchestration, and execution of automated data pipelines using **Apache Airflow** with a fully containerized environment powered by **Docker** and **Docker Compose**.

The project uses Airflow DAGs to define, schedule, and monitor workflow executions.

---

## 📌 Project Overview

Modern data platforms require reliable workflow orchestration to automate data processing tasks.

This project provides an Airflow-based environment where pipelines can be created, executed, and monitored through the Airflow Web Interface.

Key objectives:

- Automate data workflows using DAGs
- Manage pipeline scheduling and execution
- Monitor tasks and dependencies
- Run Airflow in a reproducible Docker environment

---

## 🏗️ Architecture

The project architecture is based on:
             +----------------+
             |   Data Source  |
             +----------------+
                      |
                      v
             +----------------+
             | Airflow DAGs   |
             +----------------+
                      |
                      v
             +----------------+
             | Task Execution |
             +----------------+
                      |
                      v
             +----------------+
             | Data Pipeline  |
             +----------------+


---

# 🛠️ Technologies

| Technology | Purpose |
|------------|---------|
| Apache Airflow | Workflow orchestration |
| Docker | Containerization |
| Docker Compose | Multi-container management |
| Python | Pipeline development |
| DAGs | Workflow definition |

---

# 📂 Project Structure
airflow-data-pipelines/

│
├── dags/
│ └── Airflow DAG definitions
│
├── docker-compose.yml
│
├── requirements.txt
│
├── README.md
│
└── Configuration files

---

# ✅ Prerequisites

Before installing the project, make sure you have:

- Git
- Docker
- Docker Compose

Verify installation:

```bash
docker --version
docker compose version
git --version


# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/M0iem/airflow-data-pipelines.git
```

Move into the project directory:

```bash
cd airflow-data-pipelines
```

---

## 2. Start Airflow Services

Launch the Airflow environment:

```bash
docker compose up -d
```

Docker will create and start the required containers.

---

# 🗄️ Database Initialization

Initialize the Airflow database:

```bash
docker compose run airflow-webserver airflow db init
```

Create an administrator user:

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

# 🌐 Access Airflow Interface

Open your browser:

```
http://localhost:8080
```

Credentials:

```
Username: airflow
Password: airflow
```

---

# ▶️ Running Pipelines

To execute workflows:

1. Open Airflow Web UI
2. Enable the required DAG
3. Click **Trigger DAG**
4. Monitor execution using:

   * Graph View
   * Grid View
   * Task Logs

---

# 🛑 Stop Environment

Stop all running containers:

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

# 🎯 Features

✅ Automated workflow orchestration
✅ DAG-based pipeline management
✅ Dockerized Airflow environment
✅ Task monitoring and logging
✅ Reproducible deployment setup

---

# 📚 Learning Outcomes

Through this project, the following concepts are demonstrated:

* Data pipeline orchestration
* Workflow automation
* Airflow DAG development
* Containerized environments
* Pipeline monitoring

---

# 👤 Author

**Meriem YAFIR**
