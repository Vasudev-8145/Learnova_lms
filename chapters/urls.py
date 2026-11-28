
from django.urls import path

from chapters.views import LessonCreateView
from chapters.views import LessonRetrieveUpdateDeleteView

urlpatterns = [

    # route for creating lessons
    path("modules/<int:pk>/lessons/",LessonCreateView.as_view()),

    # route to retrieve,update,delete lessons
    path("lessons/<int:pk>/",LessonRetrieveUpdateDeleteView.as_view()),
]