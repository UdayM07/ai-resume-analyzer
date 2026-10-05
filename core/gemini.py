from google import genai
from django.conf import settings
import json

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def analyze_resume(resume_text):

    prompt = f"""
You are an ATS Resume Analyzer.

Analyze the following resume.

Return exactly in this format:

ATS Score:
Summary:
Strengths:
Weaknesses:
Missing Skills:
Suggestions:

Resume:

{resume_text}
"""
    prompt = f"""
You are an ATS Resume Analyzer.

Analyze the following resume.

Return ONLY valid JSON.

{{
    "ats_score": 0,
    "summary": "",
    "strengths": "",
    "weaknesses": "",
    "missing_skills": "",
    "suggestions": ""
}}

Rules:
- ats_score must be an integer between 0 and 100.
- Return only JSON.
- Do not include markdown.
- Do not use ```json.

Resume:

{resume_text}
"""

   

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
    )

    



    return json.loads(response.text)

def analyze_job_match(resume_text, job_description, required_skills):

    prompt = f"""
You are an AI Job Matcher.

Compare the resume with the job.

Return ONLY valid JSON.

{{
    "match_score": 0,
    "matching_skills": "",
    "missing_skills": "",
    "recommendation": ""
}}

Rules:
- match_score must be between 0 and 100.
- Return only JSON.
- Do not use markdown.
- Do not use ```json.

Resume:

{resume_text}

Job Description:

{job_description}

Required Skills:

{required_skills}
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
    )

    return json.loads(response.text)