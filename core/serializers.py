from rest_framework import serializers
from .models import CustomUser,Resume
from .utils import extract_text

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

        resume.save()

        return resume