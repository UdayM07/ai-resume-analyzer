# AI Resume Analyzer & Job Matcher

An AI-powered Django REST Framework backend that enables candidates to upload resumes, receive AI-based resume analysis, match resumes with job descriptions, and apply for jobs. Recruiters can create job postings and manage applications submitted by candidates.

---

## 🚀 Live API

**Base URL**

```
https://ai-resume-analyzer-xz0n.onrender.com/api/login/
```

---

## 🔑 Demo Credentials

### Recruiter

```
Username:
recruiter

Password:
Recruiter@123
```

### Candidate

```
Username:
candidate

Password:
Candidate@123
```

> **Note:** Replace these credentials with your actual demo accounts after creating them in the deployed application.

---

# Features

## Authentication

- User Registration
- JWT Login
- Role-based Authentication
- Candidate
- Recruiter

---

## Resume Management

- Upload Resume (PDF)
- View Uploaded Resume
- Update Resume
- Delete Resume

---

## AI Resume Analysis

Google Gemini AI analyzes uploaded resumes and provides:

- Resume Summary
- ATS Score
- Missing Skills
- Improvement Suggestions

---

## Job Management

Recruiters can

- Create Job
- Update Job
- Delete Job
- View Their Jobs

---

## Job Search

Supports

- Search
- Filter
- Ordering
- Pagination

---

## AI Job Matching

Candidates can compare their resume with any job posting.

Returns

- Match Score
- Matching Skills
- Missing Skills
- AI Recommendation

---

## Job Applications

Candidates can

- Apply for Jobs
- Apply only once per job

Recruiters can

- View applicants for jobs they posted

---

# Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL (Neon)
- JWT Authentication
- Google Gemini API
- PyMuPDF
- Django Filter
- Gunicorn
- Render
- Git & GitHub

---

# API Endpoints

## Authentication

```
POST /api/register/
POST /api/login/
```

---

## Resume

```
GET    /api/resumes/
POST   /api/resumes/
PUT    /api/resumes/<id>/
DELETE /api/resumes/<id>/
```

---

## Jobs

```
GET    /api/jobs/
POST   /api/jobs/
PUT    /api/jobs/<id>/
DELETE /api/jobs/<id>/
```

---

## Applications

```
POST /api/apply/
GET  /api/recruiter/applications/
```

---

## AI

```
POST /api/resume-analysis/
POST /api/job-match/
```

---

# Search

Example

```
GET /api/jobs/?search=python
```

---

# Filter

```
GET /api/jobs/?location=Bangalore
```

```
GET /api/jobs/?company=Google
```

---

# Ordering

```
GET /api/jobs/?ordering=salary
```

```
GET /api/jobs/?ordering=-created_at
```

---

# Pagination

```
GET /api/jobs/?page=1
```

```
GET /api/jobs/?page=2
```

---

# AI Resume Analysis Flow

```
Candidate Uploads Resume
            │
            ▼
PDF Text Extraction (PyMuPDF)
            │
            ▼
Google Gemini AI
            │
            ▼
Resume Summary
ATS Score
Missing Skills
Suggestions
```

---

# AI Job Match Flow

```
Candidate Selects

Resume
+
Job

        │
        ▼

Google Gemini AI

        │
        ▼

Match Score
Matching Skills
Missing Skills
Recommendation
```

---

# Business Rules

- Only recruiters can create, update and delete jobs.
- Only candidates can apply for jobs.
- Candidates can only use their own resumes.
- Candidates can apply only once per job.
- Recruiters can only view applications submitted for their jobs.

---

# Installation

Clone the repository

```bash
git clone https://github.com/UdayM07/ai-resume-analyzer.git
```

Move into project

```bash
cd ai-resume-analyzer
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Run server

```bash
python manage.py runserver
```

---

# Environment Variables

Create a `.env` file

```
SECRET_KEY=your_secret_key

GEMINI_API_KEY=your_gemini_api_key

DATABASE_URL=your_database_url

DEBUG=True
```

---

# Deployment

- Backend: Render
- Database: Neon PostgreSQL
- Version Control: GitHub

---

# Future Improvements

- Email Verification
- Resume Version History
- Recruiter Dashboard
- Interview Scheduling
- Notifications
- AI Learning Roadmap

---

# Author

**Uday M**

GitHub

```
https://github.com/UdayM07
```

Project Repository

```
https://github.com/UdayM07/ai-resume-analyzer
```