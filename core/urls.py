from django.urls import path 


from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from .import views 

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"), 
    path("register/", views.RegisterAPI.as_view(), name="RegisterAPI"),
    path("profile/", views.PofileAPI.as_view(), name="ProfileAPI"),
    path("logout/", views.LogoutAPI.as_view(), name="logout"),
    path('changepassword/',views.ChangePasswordAPI.as_view()),
    # path("resume/upload/",views.ResumeUploadAPI.as_view(),name="resume-upload"),
    path("resumes/",views.ResumeListCreateAPI.as_view(), name="resume-list-create"),
    path("resumes/<int:pk>/",views.ResumeRetrieveUpdateDestroyAPI.as_view(),name="resume-detail",
    ),
    
    
]





