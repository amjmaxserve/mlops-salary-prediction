# 🧠 MLOps Salary Prediction Project  
### FastAPI + Streamlit + Docker + SonarQube

This project demonstrates a complete end-to-end MLOps workflow for a Salary Prediction Machine Learning application.

The application:

- Trains a Machine Learning model using scikit-learn
- Serves predictions through FastAPI
- Provides a Streamlit frontend UI
- Uses Docker for containerization
- Uses Docker Compose for orchestration
- Integrates SonarQube for code quality and static analysis

---

# 🚀 Tech Stack

| Component | Technology |
|---|---|
| Backend API | FastAPI |
| Frontend | Streamlit |
| ML Framework | scikit-learn |
| Containerization | Docker |
| Orchestration | Docker Compose |
| Code Quality | SonarQube |
| Language | Python 3.10 |

---

# 📁 Project Structure

```bash
.
├── app
│   ├── fastapi_app.py
│   └── frontend.py
│
├── model
│   ├── salary_model.pkl
│   ├── label_encoders.pkl
│   └── target_encoder.pkl
│
├── Dockerfile.base
├── Dockerfile.fastapi
├── Dockerfile.streamlit
├── docker-compose.yml
├── requirements.txt
├── train_model.py
├── sonar-project.properties
└── README.md
```

---

# ⚙️ Step 1 — Clone Repository

```bash
git clone https://github.com/amjmaxserve/mlops-salary-prediction.git

cd mlops-salary-prediction
```

---

# 🐍 Step 2 — Create Python Virtual Environment

```bash
python -m venv venv

source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

---

# 📦 Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 Step 4 — Train Machine Learning Model

Run:

```bash
python train_model.py
```

This will:

- Generate synthetic employee salary data
- Train a RandomForestClassifier
- Save trained model artifacts

Generated files:

```bash
model/
├── salary_model.pkl
├── label_encoders.pkl
└── target_encoder.pkl
```

---

# 🌐 Step 5 — Run FastAPI Backend Locally

Start FastAPI server:

```bash
uvicorn app.fastapi_app:app --host 0.0.0.0 --port 8000
```

Test API:

```bash
http://localhost:8000
```

Swagger Docs:

```bash
http://localhost:8000/docs
```

---

# 🎨 Step 6 — Run Streamlit Frontend Locally

In another terminal:

```bash
streamlit run app/frontend.py --server.port 8501
```

Open:

```bash
http://localhost:8501
```

---

# 🐳 Step 7 — Dockerization

---

## 7.1 Create Base Docker Image

### Dockerfile.base

```dockerfile
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
```

Build Base Image:

```bash
docker build -f Dockerfile.base -t ml-base-image .
```

---

## 7.2 FastAPI Dockerfile

### Dockerfile.fastapi

```dockerfile
FROM ml-base-image

WORKDIR /app

COPY . .

RUN python train_model.py

EXPOSE 8000

CMD ["uvicorn", "app.fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 7.3 Streamlit Dockerfile

### Dockerfile.streamlit

```dockerfile
FROM ml-base-image

WORKDIR /app

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app/frontend.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

# ⚙️ Step 8 — Docker Compose Setup

### docker-compose.yml

```yaml
version: '3.9'

services:

  fastapi:
    build:
      context: .
      dockerfile: Dockerfile.fastapi

    container_name: fastapi_ml_app

    ports:
      - "8000:8000"

    restart: unless-stopped

  streamlit:
    build:
      context: .
      dockerfile: Dockerfile.streamlit

    container_name: streamlit_ui

    ports:
      - "8501:8501"

    depends_on:
      - fastapi

    restart: unless-stopped
```

---

# ▶️ Step 9 — Build & Run Containers

Build:

```bash
docker compose build --no-cache
```

Run:

```bash
docker compose up -d
```

Check running containers:

```bash
docker ps
```

---

# 🌍 Application URLs

| Service | URL |
|---|---|
| Streamlit UI | http://localhost:8501 |
| FastAPI API | http://localhost:8000 |
| Swagger Docs | http://localhost:8000/docs |

---

# 🛑 Stop Containers

```bash
docker compose down
```

---

# 🔍 Step 10 — SonarQube Integration

This project supports static code analysis using SonarQube.

---

# 📁 Create Separate SonarQube Directory

```bash
mkdir -p /opt/sonarqube

cd /opt/sonarqube
```

---

# ⚙️ Create SonarQube Docker Compose

Create:

```bash
nano docker-compose.yml
```

Paste:

```yaml
version: "3.9"

services:

  sonarqube:
    image: sonarqube:community
    container_name: sonarqube

    depends_on:
      - postgres

    environment:
      SONAR_JDBC_URL: jdbc:postgresql://postgres:5432/sonarqube
      SONAR_JDBC_USERNAME: sonar
      SONAR_JDBC_PASSWORD: sonarpassword

    ports:
      - "9000:9000"

    volumes:
      - sonarqube_data:/opt/sonarqube/data
      - sonarqube_logs:/opt/sonarqube/logs
      - sonarqube_extensions:/opt/sonarqube/extensions

    restart: unless-stopped

  postgres:
    image: postgres:15
    container_name: sonarqube-postgres

    environment:
      POSTGRES_USER: sonar
      POSTGRES_PASSWORD: sonarpassword
      POSTGRES_DB: sonarqube

    volumes:
      - postgres_data:/var/lib/postgresql/data

    restart: unless-stopped

volumes:
  sonarqube_data:
  sonarqube_logs:
  sonarqube_extensions:
  postgres_data:
```

---

# 🔧 Linux Kernel Configuration

SonarQube requires Linux kernel tuning.

Run:

```bash
sudo sysctl -w vm.max_map_count=524288

sudo sysctl -w fs.file-max=131072
```

Persist settings:

```bash
sudo nano /etc/sysctl.conf
```

Add:

```bash
vm.max_map_count=524288
fs.file-max=131072
```

Apply:

```bash
sudo sysctl -p
```

---

# ▶️ Start SonarQube

```bash
cd /opt/sonarqube

docker compose up -d
```

Verify:

```bash
docker ps
```

---

# 🌍 Access SonarQube

Open:

```bash
http://SERVER_IP:9000
```

Default Credentials:

```text
Username: admin
Password: admin
```

Change password after first login.

---

# 🔑 Generate SonarQube Token

Go to:

```text
My Account → Security → Generate Token
```

Copy generated token.

Example:

```text
sqa_xxxxxxxxxxxxxxxxxxxxxxxxx
```

---

# 📄 Step 11 — Create sonar-project.properties

Inside project root:

```bash
nano sonar-project.properties
```

Add:

```properties
sonar.projectKey=salary-prediction-mlops

sonar.projectName=Salary Prediction MLOps

sonar.projectVersion=1.0

sonar.sources=.

sonar.sourceEncoding=UTF-8

sonar.python.version=3

sonar.exclusions=**/__pycache__/**,**/.venv/**,**/venv/**,**/*.ipynb,**/model/**

sonar.python.coverage.reportPaths=coverage.xml
```

---

# 🧪 Step 12 — Generate Coverage Report

Install testing tools:

```bash
pip install pytest pytest-cov
```

Generate coverage:

```bash
pytest --cov=. --cov-report=xml
```

This creates:

```bash
coverage.xml
```

---

# 🔍 Step 13 — Run Sonar Scanner

From project root:

```bash
docker run --rm \
  -e SONAR_HOST_URL="http://192.168.29.7:9000" \
  -e SONAR_TOKEN="YOUR_TOKEN" \
  -v "$(pwd):/usr/src" \
  sonarsource/sonar-scanner-cli
```

---

# ✅ Successful Scan Output

Expected output:

```bash
ANALYSIS SUCCESSFUL
```

Dashboard:

```bash
http://SERVER_IP:9000/dashboard?id=salary-prediction-mlops
```

---

# 📊 SonarQube Features

The scan provides:

- Bugs
- Vulnerabilities
- Code Smells
- Security Hotspots
- Coverage Reports
- Maintainability Metrics
- Duplication Detection

---

# 🛠️ Common Commands

| Action | Command |
|---|---|
| Train Model | `python train_model.py` |
| Run FastAPI | `uvicorn app.fastapi_app:app --reload` |
| Run Streamlit | `streamlit run app/frontend.py` |
| Build Docker Images | `docker compose build` |
| Start Containers | `docker compose up -d` |
| Stop Containers | `docker compose down` |
| Generate Coverage | `pytest --cov=. --cov-report=xml` |
| Sonar Scan | `docker run --rm -e SONAR_HOST_URL=<url> -e SONAR_TOKEN=<token> -v "$(pwd):/usr/src" sonarsource/sonar-scanner-cli` |

---

# 🚀 Future Improvements

Recommended next enhancements:

- GitHub Actions CI/CD
- Jenkins Pipelines
- Kubernetes Deployment
- Terraform Infrastructure
- DVC Model Versioning
- MLflow Tracking
- Prometheus Monitoring
- Grafana Dashboards
- Trivy Security Scanning
- Bandit Python Security Analysis

---

# 🎯 Conclusion

This project demonstrates a complete production-style MLOps workflow:

```text
Data → Training → Model Serialization → API → Frontend →
Docker → Docker Compose → SonarQube → DevSecOps
```

The architecture is scalable, reproducible, and cloud-ready.

---

# 👨‍💻 Author

Arjun M J

- DevOps Engineer
- Cloud Architect
- Cyber Forensics Analyst

Certifications:

- AWS Solution Architect Associate
- AWS Security Specialty
- RCCE Certified Cyber Security Engineer

---
