
from django.urls import path

from accounts.views import TrainerCreateView,StudentCreateView

urlpatterns = [

    # route for trainer creation
    path("trainer/",TrainerCreateView.as_view()),

    # route for student creation
    path("student/",StudentCreateView.as_view()),
]