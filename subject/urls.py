
from django.urls import path

from subject.views import CourseListView,CourseCreateView
from subject.views import CourseRetrieveView,CourseUpdateDeleteView

urlpatterns = [

    # route to listing courses
    path("course/all/",CourseListView.as_view()),

    # route to course creation
    path("course/add/",CourseCreateView.as_view()),

    # route to course retreiving
    path("course/one/<int:pk>/",CourseRetrieveView.as_view()),

    # route to course update,delete
    path("course/<int:pk>/",CourseUpdateDeleteView.as_view()),
]