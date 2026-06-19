# CloudOps AI Copilot

CloudOps AI Copilot is an AI-powered assistant designed to help engineers, students, and cloud practitioners with AWS, Linux, DevOps, Docker, Kubernetes, Terraform, and infrastructure-related tasks.

The application consists of:

* FastAPI backend API
* Streamlit frontend UI
* Dockerized deployment
* Jenkins CI/CD pipeline
* GitHub Webhook integration
* AWS EC2 hosting

---

## Architecture

```text
GitHub
   │
   ▼
GitHub Webhook
   │
   ▼
Jenkins CI/CD
   │
   ▼
Docker Compose
   │
   ├── FastAPI API (Port 8000)
   └── Streamlit UI (Port 8501)
   │
   ▼
AWS EC2
```

---

## Features

* Cloud Operations Assistant
* AWS Knowledge Base
* Linux Troubleshooting Support
* Docker & Kubernetes Guidance
* Terraform Assistance
* Infrastructure Architecture Suggestions
* AI-Powered Cloud Support Chat
* Automated CI/CD Deployment

---

## Tech Stack

### Backend

* FastAPI
* Python
* Uvicorn

### Frontend

* Streamlit

### DevOps

* Docker
* Docker Compose
* Jenkins
* GitHub Webhooks

### Cloud

* AWS EC2

---

## Project Structure

```text
cloudops-ai-copilot/
│
├── frontend/
│   └── app.py
│
├── services/
│
├── models/
│
├── rag/
│
├── knowledge/
│   ├── aws/
│   ├── devops/
│   └── linux/
│
├── database/
│
├── Dockerfile
├── Dockerfile.streamlit
├── docker-compose.yml
├── Jenkinsfile
├── requirements.txt
└── main.py
```

---

## Local Setup

Clone the repository:

```bash
git clone https://github.com/vkkprathik/cloudops-ai-copilot.git
cd cloudops-ai-copilot
```

Create environment file:

```bash
touch .env
```

Add:

```env
GROQ_API_KEY=your_api_key
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI:

```bash
uvicorn main:app --reload
```

Run Streamlit:

```bash
streamlit run frontend/app.py
```

---

## Docker Deployment

Build and start containers:

```bash
docker compose up -d --build
```

Check containers:

```bash
docker ps
```

Stop containers:

```bash
docker compose down
```

---

## CI/CD Pipeline

The project uses Jenkins and GitHub Webhooks for automatic deployment.

Workflow:

1. Push code to GitHub
2. GitHub triggers Webhook
3. Jenkins starts pipeline
4. Docker images are rebuilt
5. Application is redeployed automatically

---

## Jenkins Pipeline

Stages:

* Checkout
* Build Docker Images
* Deploy Application
* Verify Deployment

---

## Deployment

Hosted on AWS EC2 using Docker Compose.

Services:

* FastAPI API → Port 8000
* Streamlit UI → Port 8501
* Jenkins → Port 8080

---

## Author

Prathik Kulkarni

LinkedIn:
https://linkedin.com/in/prathik-kulkarni-396775301

GitHub:
https://github.com/vkkprathik

