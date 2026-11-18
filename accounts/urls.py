
from django.urls import path

from accounts.views import TrainerCreateView,StudentCreateView
from accounts.views import TrainerProfileUpdateView,TrainerprofileGetView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [

    # route for trainer creation
    path("trainer/",TrainerCreateView.as_view()),

    # route for student creation
    path("student/",StudentCreateView.as_view()),

    # route for token creation
    path("token/",ObtainAuthToken.as_view()),

    # route for trainer profile updation
    path("trainer/profile/complete/",TrainerProfileUpdateView.as_view()),

    # route for trainer profile detailing
    path("trainer/profile/me/",TrainerprofileGetView.as_view()),
]