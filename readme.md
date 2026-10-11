# AI Resume Analyzer & Job Matcher

An AI-powered Django REST Framework application that helps candidates analyze resumes, match them with job descriptions, and apply for jobs, while allowing recruiters to manage job postings and review applicants.

---

## Features

### Authentication
- JWT Authentication
- User Registration
- User Login
- Role-based Access (Candidate & Recruiter)

### Resume Management
- Upload PDF Resume
- Update Resume
- Delete Resume
- View Uploaded Resume
- PDF Text Extraction using PyMuPDF

### AI Resume Analysis
- Resume analysis using Google Gemini AI
- Resume summary generation
- ATS Score
- Missing Skills Detection
- Resume Improvement Suggestions

### Job Management
- Recruiters can Create Jobs
- Update Jobs
- Delete Jobs
- View Jobs

### Job Search
- Search Jobs
- Filter Jobs
- Order Jobs
- Pagination

### AI Job Matching
- Compare Resume with Job Description
- Match Score
- Matching Skills
- Missing Skills
- AI Recommendation

### Job Applications
- Apply for Jobs
- Duplicate Application Prevention
- Resume Ownership Validation
- Recruiters can view applicants for their jobs

---

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- Google Gemini API
- PyMuPDF
- Django Filter
- Git & GitHub

---

## Project Structure

```
ai_resume_analyzer/
│
├── config/
│
├── core/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── gemini.py
│   ├── urls.py
│   └── utils.py
│
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

## API Features

### Authentication
- Register
- Login

### Resume
- Upload Resume
- List Resume
- Update Resume
- Delete Resume

### Jobs
- Create Job
- List Jobs
- Update Job
- Delete Job

### Applications
- Apply for Job
- Recruiter Applicant List

### AI
- Resume Analysis
- Job Match

---

## Search

Example

```
GET /api/jobs/?search=python
```

---

## Filter

Example

```
GET /api/jobs/?location=Bangalore
```

```
GET /api/jobs/?company=Google
```

---

## Ordering

Example

```
GET /api/jobs/?ordering=salary
```

```
GET /api/jobs/?ordering=-created_at
```

---

## Pagination

Example

```
GET /api/jobs/?page=1
```

```
GET /api/jobs/?page=2
```

---

## AI Resume Analysis Flow

Candidate uploads a PDF resume

↓

PyMuPDF extracts text from the resume

↓

Google Gemini AI analyzes the extracted content

↓

The system generates:

- Resume Summary
- ATS Score
- Missing Skills
- Improvement Suggestions

---

## AI Job Match Flow

Candidate selects

- Resume
- Job

↓

Gemini AI compares

- Resume Skills
- Required Job Skills

↓

Returns

- Match Score
- Matching Skills
- Missing Skills
- Recommendation

---

## Business Rules

- Only Recruiters can create, update and delete jobs.
- Only Candidates can apply for jobs.
- Candidates can apply only once per job.
- Candidates can only use their own resumes.
- Recruiters can only view applications for jobs they created.

---

## Installation

Clone Repository

```bash
git clone https://github.com/UdayM07/ai-resume-analyzer.git
```

Move into project

```bash
cd ai-resume-analyzer
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Migrations

```bash
python manage.py migrate
```

Start Server

```bash
python manage.py runserver
```

---

## Environment Variables

Create a `.env` file in the project root.

```
SECRET_KEY=your_secret_key

GEMINI_API_KEY=your_gemini_api_key
```

---

## Future Improvements

- Email Verification
- Resume Versioning
- Recruiter Dashboard
- Interview Scheduling
- Notifications
- AI Skill Gap Learning Roadmap

---

## Author

**Uday M**

GitHub

https://github.com/UdayM07