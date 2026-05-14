# 🧠 MLOps Salary Prediction App

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-FF4B4B.svg)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-24.0+-2496ED.svg)](https://www.docker.com/)

A complete MLOps project that trains a Random Forest classifier on synthetic salary data, exposes a REST API with FastAPI, and provides an interactive UI via Streamlit. The entire application is containerized with Docker and orchestrated using Docker Compose. Optionally integrate SonarQube for static code analysis.

---

## 📁 Project Structure

├── app
│ ├── fastapi_app.py # FastAPI backend (prediction endpoint)
│ └── frontend.py # Streamlit frontend UI
├── docker-compose.yml # Orchestrates FastAPI + Streamlit
├── Dockerfile.base # Base Python image with dependencies
├── Dockerfile.fastapi # FastAPI service image
├── Dockerfile.streamlit # Streamlit service image
├── model # Saved models (created after training)
│ ├── salary_model.pkl
│ ├── label_encoders.pkl
│ └── target_encoder.pkl
├── requirements.txt # Python dependencies
├── train_model.py # Data generation & model training script
└── sonar-project.properties # SonarQube configuration (optional)

---

