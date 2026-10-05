from rest_framework import serializers
from .models import CustomUser,Resume,Job,JobMatch,Application
from .utils import extract_text
from .gemini import analyze_resume, analyze_job_match

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(write_only=True)
    class Meta:
        model=CustomUser
        fields=(
            'username',
            'email',
            'first_name',
            'last_name',
            'role',
            'password',
            'confirm_password',
        )
        extra_kwargs={
            'password':{'write_only':True},
        }

    def validate(self, attrs):
       if attrs['password']!=attrs['confirm_password']:
        raise serializers.ValidationError(
            {'password':'Password do not match'}
        )
       return attrs

    def validate_password(self,a):
       if len(a)<8:
          raise serializers.ValidationError(
                      {'password':'It must be minimum 8 Characters'}
                  )
       return a

    def validate_email(self,a):
       if CustomUser.objects.filter(email=a).exists():
          raise serializers.ValidationError(
             {'email':'Email already exists'}
          )
       return a  

    def validate_username(self,a):
       if CustomUser.objects.filter(username=a).exists():
          raise serializers.ValidationError(
             {'username':'Username alreadye exists '}
          )
       return a

    def create(self, validated_data):
       validated_data.pop('confirm_password')
       user=CustomUser.objects.create_user(**validated_data)
       return user

class ProfileSerializer(serializers.ModelSerializer):
   class Meta:
      model=CustomUser
              
      fields=(
            'username',
            'email',
            'first_name',
            'last_name',
            'role',
        )

      
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs["new_password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match."}
            )
        return attrs


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class ResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume

        fields = (
            "id",
            "title",
            "resume_file",
            "uploaded_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "uploaded_at",
            "updated_at",
        )

    def create(self, validated_data):

        user = self.context["request"].user

        resume = Resume.objects.create(
            user=user,
            **validated_data
        )
        

        text = extract_text(resume.resume_file)
        
        resume.extracted_text = text
        
        

        try:
            analysis = analyze_resume(text)
            

            resume.ats_score = analysis.get("ats_score")
            resume.summary = analysis.get("summary")
            resume.strengths = analysis.get("strengths")
            resume.weaknesses = analysis.get("weaknesses")
            resume.missing_skills = analysis.get("missing_skills")
            resume.suggestions = analysis.get("suggestions")

        except Exception as e:
          

            resume.summary = "AI analysis is temporarily unavailable."

        resume.save()

        return resume



class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job

        fields = (
            "id",
            "title",
            "company",
            "description",
            "required_skills",
            "location",
            "salary",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )

    def create(self, validated_data):

        user = self.context["request"].user

        job = Job.objects.create(
            user=user,
            **validated_data
        )

        return job
    
class JobMatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobMatch

        fields = (
            "id",
            "resume",
            "job",
            "match_score",
            "matching_skills",
            "missing_skills",
            "recommendation",
            "created_at",
        )

        read_only_fields = (
            "id",
            "match_score",
            "matching_skills",
            "missing_skills",
            "recommendation",
            "created_at",
        )

    def create(self, validated_data):

     resume = validated_data["resume"]
     job = validated_data["job"]

     try:
        analysis = analyze_job_match(
            resume.extracted_text,
            job.description,
            job.required_skills,
        )

        match = JobMatch.objects.create(
            resume=resume,
            job=job,
            match_score=analysis.get("match_score"),
            matching_skills=analysis.get("matching_skills"),
            missing_skills=analysis.get("missing_skills"),
            recommendation=analysis.get("recommendation"),
        )

     except Exception as e:

        

        match = JobMatch.objects.create(
            resume=resume,
            job=job,
            match_score=0,
            matching_skills="",
            missing_skills="",
            recommendation="AI analysis is temporarily unavailable.",
        )

     return match

class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = (
            "id",
            "job",
            "resume",
            "applied_at",
        )
        read_only_fields = (
            "id",
            "applied_at",
        )

    def validate(self, attrs):

     candidate = self.context["request"].user
     job = attrs["job"]
     resume = attrs["resume"]

     if Application.objects.filter(
        candidate=candidate,
        job=job
     ).exists():
        raise serializers.ValidationError(
            {
                "detail": "You have already applied for this job."
            }
        )

     if resume.user != candidate:
        raise serializers.ValidationError(
            {
                "resume": "You can only use your own resume."
            }
        )

     return attrs

    def create(self, validated_data):

        candidate = self.context["request"].user

        return Application.objects.create(
            candidate=candidate,
            **validated_data
        )

class RecruiterApplicationSerializer(serializers.ModelSerializer):

    candidate = serializers.CharField(source="candidate.username", read_only=True)
    job = serializers.CharField(source="job.title", read_only=True)
    resume = serializers.CharField(source="resume.title", read_only=True)

    class Meta:
        model = Application

        fields = (
            "id",
            "candidate",
            "job",
            "resume",
            "applied_at",
        )