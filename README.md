🚀 EvalFlow AI
AI-Powered LLM Evaluation Platform

A Full-Stack AI Platform for Automated Large Language Model (LLM) Evaluation, Analytics, and Performance Benchmarking

🌟 Overview

EvalFlow AI is a Full-Stack AI-powered LLM Evaluation Platform built to automate the benchmarking of Large Language Models (LLMs).

Instead of manually testing prompts one by one, users simply upload a CSV dataset containing prompts, choose an AI model, and the platform automatically evaluates every prompt while collecting valuable performance metrics.

The platform securely stores evaluation history, generates analytics dashboards, exports professional PDF reports, and follows a scalable layered architecture suitable for enterprise applications.

✨ Key Features
🔐 Authentication
JWT Authentication
Secure Login & Registration
Password Hashing (bcrypt)
Protected REST APIs
Authorization & Ownership Verification
📂 Dataset Management
CSV Upload
Drag & Drop Upload
Automatic Prompt Detection
Dataset Validation
Secure Dataset Storage
Dataset History
🤖 AI Evaluation Engine
Google Gemini Integration
Batch Prompt Evaluation
Automatic Response Generation
Latency Measurement
Token Usage Tracking
Estimated Cost Calculation
Retry Logic
Error Handling
📊 Analytics Dashboard
Total Evaluations
Completed Evaluations
Pending Evaluations
Failed Evaluations
Average Latency
Token Usage
Estimated Cost
Success Rate
Evaluation History
📄 PDF Report Generation

Generate professional downloadable reports including:

Evaluation Summary
Dataset Details
AI Responses
Latency Statistics
Token Usage
Estimated Cost
Performance Summary
🔍 Search & Pagination
Search Evaluations
Filter Results
Server-side Pagination
Sorting
Fast Retrieval
🚀 Continuous Integration

Implemented using GitHub Actions

Automatic

Dependency Installation
Build Verification
Workflow Validation
🏗️ Architecture
                     React Frontend
                            │
                            ▼
                     Axios REST APIs
                            │
                            ▼
                     FastAPI Backend
                            │
         ┌──────────────────┼──────────────────┐
         ▼                  ▼                  ▼
 Authentication      Dataset Service    Evaluation Service
                                               │
                                               ▼
                                        Evaluation Engine
                                               │
                                               ▼
                                         Google Gemini
                                               │
                                               ▼
                                             MySQL
🛠 Tech Stack
Frontend
React.js
Vite
Tailwind CSS
Axios
React Router
Backend
FastAPI
SQLAlchemy ORM
JWT Authentication
Pydantic
bcrypt
AI
Google Gemini API
Prompt Evaluation Engine
Token Counter
Cost Estimation
Database
MySQL
DevOps
Git
GitHub
GitHub Actions
📂 Project Structure
EvalFlow-AI

├── backend
│   ├── app
│   │   ├── api
│   │   ├── core
│   │   ├── database
│   │   ├── evaluation
│   │   ├── models
│   │   ├── schemas
│   │   ├── services
│   │   ├── uploads
│   │   └── main.py
│
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   ├── services
│   │   ├── hooks
│   │   └── App.jsx
│
├── .github
│   └── workflows
│
└── README.md
⚙️ Workflow
User Login
     │
     ▼
Upload Dataset
     │
     ▼
Validate CSV
     │
     ▼
Extract Prompts
     │
     ▼
Gemini Evaluation
     │
     ▼
Measure Latency
     │
     ▼
Count Tokens
     │
     ▼
Estimate Cost
     │
     ▼
Store Results
     │
     ▼
Analytics Dashboard
     │
     ▼
Generate PDF Report
📊 Metrics Captured

For every evaluated prompt, EvalFlow AI records:

AI Response
Response Latency
Input Tokens
Output Tokens
Total Tokens
Estimated API Cost
Evaluation Status
🔒 Security
JWT Authentication
bcrypt Password Hashing
SQLAlchemy ORM
Protected APIs
Parameterized Queries
Environment Variables
Dataset Ownership Verification
⚡ Performance Optimizations
Layered Architecture
Modular Service Layer
Server-side Pagination
Optimized SQL Queries
Efficient Database Relationships
Retry Logic
Batch Evaluation
📈 Dashboard Analytics

The dashboard provides:

Total Evaluations
Completed Evaluations
Pending Evaluations
Average Latency
Token Usage
Estimated Cost
Success Rate
Recent Evaluation History
📄 PDF Export

Generate professional reports containing:

Evaluation Summary
Dataset Information
Model Information
Prompt Responses
Latency Statistics
Token Usage
Cost Analysis
🚀 CI Pipeline
Git Push
    │
    ▼
GitHub Actions
    │
    ▼
Install Dependencies
    │
    ▼
Validate Project
    │
    ▼
Build Verification
📸 Screenshots

Replace these images with your own screenshots.

🔐 Login Page
<img src="docs/screenshots/login.png" width="100%"/>
📊 Dashboard
<img src="docs/screenshots/dashboard.png" width="100%"/>
📂 Dataset Upload
<img src="docs/screenshots/upload.png" width="100%"/>
🤖 Evaluation
<img src="docs/screenshots/evaluation.png" width="100%"/>
📈 Analytics
<img src="docs/screenshots/analytics.png" width="100%"/>
📄 PDF Report
<img src="docs/screenshots/report.png" width="100%"/>
🚀 Getting Started
Clone Repository
git clone https://github.com/yourusername/EvalFlow-AI.git

cd EvalFlow-AI
Backend
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
Frontend
cd frontend

npm install

npm run dev
Environment Variables

Create a .env file inside the backend directory.

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

GEMINI_MODEL=gemini-2.5-flash
🎯 Project Highlights
✅ Full-Stack AI Application
✅ JWT Authentication
✅ Google Gemini Integration
✅ Automated Prompt Evaluation
✅ Analytics Dashboard
✅ PDF Report Generation
✅ Token Usage Tracking
✅ Latency Measurement
✅ Estimated Cost Calculation
✅ Search & Pagination
✅ CI Pipeline with GitHub Actions
✅ Layered Enterprise Architecture
📌 Future Enhancements
Multi-LLM Support (OpenAI, Claude, Llama)
AI Judge for Automatic Response Scoring
Retrieval-Augmented Generation (RAG)
Redis Caching
Background Workers
Docker Support
Kubernetes Deployment
WebSocket Live Progress
Team Collaboration
Role-Based Access Control (RBAC)
🎓 Skills Demonstrated
Full Stack Development
FastAPI
React.js
REST API Development
SQLAlchemy ORM
JWT Authentication
MySQL
AI Integration
Google Gemini API
Prompt Engineering
LLM Evaluation
Analytics Dashboard Development
CI/CD with GitHub Actions
Software Architecture
Performance Optimization
🤝 Contributing

Contributions are welcome.

Feel free to fork this repository and submit a Pull Request.

📄 License

This project is licensed under the MIT License.

👨‍💻 Author

Aayush Pant

B.Tech – Computer Science & Engineering

Graphic Era Hill University
