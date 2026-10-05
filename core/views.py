from .models import CustomUser,Resume,Job,Application
from .serializers import RegisterSerializer,ProfileSerializer,ChangePasswordSerializer,LogoutSerializer,ResumeSerializer,JobSerializer,JobMatchSerializer,ApplicationSerializer,RecruiterApplicationSerializer
from .permissions import IsRecruiter
# from .permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCandidate
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class RegisterAPI(generics.CreateAPIView):
    serializer_class=RegisterSerializer 

class PofileAPI(generics.RetrieveAPIView): 
    queryset=CustomUser.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        return self.request.user



class ChangePasswordAPI(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user

        if not user.check_password(serializer.validated_data["old_password"]):
            return Response(
                {"old_password": "Old password is incorrect."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.set_password(serializer.validated_data["new_password"])
        user.save()

        return Response(
            {"message": "Password changed successfully."},
            status=status.HTTP_200_OK,
        )

class LogoutAPI(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            refresh_token = serializer.validated_data["refresh"]

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message": "Logout successful."},
                status=status.HTTP_200_OK,
            )

        except Exception:
            return Response(
                {"error": "Invalid refresh token."},
                status=status.HTTP_400_BAD_REQUEST,
            )

class ResumeUploadAPI(generics.CreateAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {
            "request": self.request
        }



class ResumeListCreateAPI(generics.ListCreateAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        return {"request": self.request}


class ResumeRetrieveUpdateDestroyAPI(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        return {"request": self.request}


class JobCreateListAPI(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]


    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]

    search_fields = [
        "title",
        "company",
        "location",
        "required_skills",
    ]

    filterset_fields = [
        "location",
        "company",
    ]

    ordering_fields = [
        "created_at",
        "salary",
        "title",
    ]

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsRecruiter()]
        return [IsAuthenticated()]




   
    def get_queryset(self):
        return Job.objects.all()

    def get_serializer_context(self):
        return {
            "request": self.request
        }

class JobRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
    permission_classes = [IsRecruiter]

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)

class JobMatchAPI(generics.CreateAPIView):
    serializer_class = JobMatchSerializer
    permission_classes = [IsAuthenticated]


class ApplicationCreateListAPI(generics.ListCreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsCandidate]

    def get_queryset(self):
        return Application.objects.filter(
            candidate=self.request.user
        )

    def get_serializer_context(self):
        return {
            "request": self.request
        }

class RecruiterApplicationListAPI(generics.ListAPIView):

    serializer_class = RecruiterApplicationSerializer
    permission_classes = [IsRecruiter]

    def get_queryset(self):
        return Application.objects.filter(
            job__user=self.request.user
        )