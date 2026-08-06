# 🚀 EvalFlow AI

AI-Powered LLM Evaluation Platform

> **A Full-Stack AI Platform for Automated Large Language Model (LLM) Evaluation, Analytics, and Performance Benchmarking**

# 🌟 Overview

EvalFlow AI is a full-stack AI-powered LLM Evaluation Platform designed to automate the benchmarking of Large Language Models (LLMs). Instead of manually testing prompts one by one, users can upload a CSV dataset containing hundreds of prompts and automatically evaluate them using Google's Gemini AI.

The platform measures response latency, token usage, estimated API cost, and stores complete evaluation history. It also provides an analytics dashboard, PDF report generation, search, filtering, pagination, and secure JWT-based authentication.

EvalFlow AI follows a modular layered architecture, making it scalable, maintainable, and easy to extend with future AI providers and enterprise features.

---

# ✨ Features

## 🔐 Authentication

- User Registration
- Secure Login
- JWT Authentication
- Password Hashing (bcrypt)
- Protected REST APIs
- Authorization & Access Control

---

## 📂 Dataset Management

- CSV Upload
- Drag & Drop Upload
- Automatic Prompt Column Detection
- Dataset Validation
- Dataset Ownership Verification
- Dataset History

---

## 🤖 AI Evaluation Engine

- Google Gemini Integration
- Batch Prompt Evaluation
- Sequential Processing
- Retry Logic for Rate Limits
- Exception Handling
- Response Storage
- Token Counting
- Latency Measurement
- Cost Estimation

---

## 📊 Analytics Dashboard

- Total Evaluations
- Completed Evaluations
- Pending Evaluations
- Failed Evaluations
- Average Latency
- Total Token Usage
- Estimated Cost
- Evaluation History

---

## 📄 PDF Report Generation

Generate downloadable reports including:

- Evaluation Summary
- Dataset Information
- Model Information
- Prompt Responses
- Latency Statistics
- Token Usage
- Estimated Cost
- Overall Summary

---

## 🔍 Search, Filter & Pagination

- Search Evaluations
- Filter by Status
- Server-side Pagination
- Sorting
- Fast Data Retrieval

---

## 🚀 CI Pipeline

GitHub Actions automatically performs:

- Dependency Installation
- Project Validation
- Build Verification

---

# 🏗️ System Architecture

```text
                    React Frontend
                           │
                           ▼
                    REST APIs (Axios)
                           │
                           ▼
                    FastAPI Backend
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
 Authentication     Dataset Service   Evaluation Service
                                              │
                                              ▼
                                       Evaluation Engine
                                              │
                                              ▼
                                         Google Gemini
                                              │
                                              ▼
                                           MySQL
```

---

# 🛠 Tech Stack

## Frontend

- React.js
- Vite
- Tailwind CSS
- Axios
- React Router

---

## Backend

- FastAPI
- SQLAlchemy ORM
- JWT Authentication
- Pydantic
- bcrypt

---

## AI & Machine Learning

- Google Gemini API
- Prompt Evaluation Engine
- Token Counter
- Cost Estimator

---

## Database

- MySQL

---

## DevOps

- Git
- GitHub
- GitHub Actions (CI)

---

# 📂 Project Structure

```text
EvalFlow-AI/

├── backend/
│
│   ├── app/
│   │
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── evaluation/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── uploads/
│   └── main.py
│
├── frontend/
│
│   ├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── hooks/
│   └── App.jsx
│
├── .github/
│   └── workflows/
│
└── README.md
```

---

# ⚙️ Workflow

```text
User Login
      │
      ▼
Upload CSV Dataset
      │
      ▼
Dataset Validation
      │
      ▼
Prompt Extraction
      │
      ▼
Gemini AI Evaluation
      │
      ▼
Latency Measurement
      │
      ▼
Token Counting
      │
      ▼
Cost Estimation
      │
      ▼
Store Results
      │
      ▼
Analytics Dashboard
      │
      ▼
Generate PDF Report
```

---

# 🗄 Database Schema

```text
Users
  │
  │ 1:N
  ▼
Datasets
  │
  │ 1:N
  ▼
Evaluations
  │
  │ 1:N
  ▼
Evaluation Results
```

---

# 📈 Metrics Captured

For every prompt, EvalFlow AI records:

- AI Response
- Response Latency
- Input Tokens
- Output Tokens
- Total Tokens
- Estimated API Cost
- Evaluation Status

---

# 🔒 Security Features

- JWT Authentication
- bcrypt Password Hashing
- Protected REST APIs
- SQLAlchemy ORM
- Parameterized Queries
- Input Validation
- Dataset Ownership Verification
- Environment Variables

---

# ⚡ Performance Optimizations

- Server-side Pagination
- Optimized SQL Queries
- Layered Architecture
- Modular Service Layer
- Retry Logic
- Efficient Database Relationships
- Token Counting
- Cost Estimation

---

# 📊 Dashboard Analytics

The dashboard provides:

- Total Evaluations
- Completed Evaluations
- Pending Evaluations
- Failed Evaluations
- Average Latency
- Estimated Token Usage
- Estimated API Cost
- Evaluation History

---

# 📄 PDF Export

Generate professional evaluation reports containing:

- Evaluation Summary
- Dataset Details
- Provider Information
- Model Details
- Prompt Responses
- Latency Statistics
- Token Usage
- Cost Estimation

---

# 🚀 CI Pipeline

GitHub Actions automatically performs:

```text
Git Push
     │
     ▼
GitHub Actions
     │
     ▼
Checkout Repository
     │
     ▼
Install Dependencies
     │
     ▼
Project Validation
     │
     ▼
Build Verification
```

---

# 📸 Screenshots

## 🔐 Login Page

<img src="docs/screenshots/login.png" width="100%">

---

## 📊 Dashboard

<img src="docs/screenshots/dashboard.png" width="100%">

---

## 📂 Dataset Upload

<img src="docs/screenshots/upload.png" width="100%">

---

## 🤖 Evaluation

<img src="docs/screenshots/evaluation.png" width="100%">

---

## 📈 Analytics

<img src="docs/screenshots/analytics.png" width="100%">

---

## 📄 PDF Report

<img src="docs/screenshots/report.png" width="100%">

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/yourusername/EvalFlow-AI.git

cd EvalFlow-AI
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

## Environment Variables

Create a `.env` file inside the backend folder.

```env
SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

DB_HOST=localhost

DB_PORT=3306

DB_USER=root

DB_PASSWORD=

DB_NAME=evalflow_ai

UPLOAD_FOLDER=backend/uploads

GEMINI_API_KEY=your_gemini_api_key

GEMINI_MODEL=gemini-2.5-flash-lite
```

---

# 🎯 Project Highlights

- ✅ Full Stack AI-Powered Web Application
- ✅ JWT-Based Authentication
- ✅ AI Integration with Google Gemini
- ✅ Automated Prompt Evaluation
- ✅ Response Latency Measurement
- ✅ Token Usage Tracking
- ✅ Estimated Cost Calculation
- ✅ Analytics Dashboard
- ✅ PDF Report Generation
- ✅ Search, Filtering & Pagination
- ✅ Modular Layered Architecture
- ✅ CI Pipeline with GitHub Actions

---

# 📌 Future Roadmap

- Multi-LLM Support (OpenAI, Claude, Llama)
- AI Judge for Response Scoring
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Redis Caching
- Background Workers
- Docker Deployment
- Kubernetes Orchestration
- WebSocket Live Progress
- Cloud Storage Integration
- Role-Based Access Control (RBAC)
- Team Collaboration Workspace

---

# 🎓 Skills Demonstrated

- Full Stack Development
- FastAPI
- React.js
- REST API Development
- JWT Authentication
- SQLAlchemy ORM
- Database Design
- MySQL
- Google Gemini API
- Prompt Engineering
- LLM Evaluation
- Analytics Dashboard Development
- PDF Report Generation
- Git & GitHub
- GitHub Actions (CI)
- Software Architecture
- Performance Optimization

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve EvalFlow AI, feel free to fork the repository, create a feature branch, and submit a pull request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Aayush Pant**

B.Tech – Computer Science & Engineering

Graphic Era Hill University

📧 Email: your-email@example.com

🔗 LinkedIn: https://linkedin.com/in/your-profile

💻 GitHub: https://github.com/yourusername

---

# ⭐ If you found this project useful, don't forget to Star the repository!
