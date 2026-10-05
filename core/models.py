from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):

    ROLE_CHOICES=[
       
        ('candidate','Candidate'),
        ('recruiter','Recruiter'),
    ]
    
    email=models.EmailField( max_length=254,unique=True)
    role=models.CharField(max_length=100,choices=ROLE_CHOICES,default='candidate')
    is_email_verified=models.BooleanField(default=False)

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="resumes",)
    title = models.CharField(max_length=255)
    resume_file = models.FileField(upload_to="resumes/",null=True,blank=True)
    extracted_text = models.TextField(blank=True)
    ats_score = models.IntegerField(null=True, blank=True)
    summary = models.TextField(blank=True)
    strengths = models.TextField(blank=True)
    weaknesses = models.TextField(blank=True)
    missing_skills = models.TextField(blank=True)
    suggestions = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




class Job(models.Model):

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "recruiter"},
        related_name="jobs",
    )

    title = models.CharField(max_length=255)

    company = models.CharField(max_length=255)

    description = models.TextField()

    required_skills = models.TextField()

    location = models.CharField(max_length=255)

    salary = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class JobMatch(models.Model):

    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="matches"
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="matches"
    )

    match_score = models.IntegerField()

    matching_skills = models.TextField()

    missing_skills = models.TextField()

    recommendation = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.resume.title} - {self.job.title}"
    

class Application(models.Model):

    candidate = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    applied_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["candidate", "job"],
                name="unique_candidate_job"
            )
        ]

    def __str__(self):
        return f"{self.candidate.username} - {self.job.title}"