
from django.urls import path

from units.views import ModuleCreateView,ModuleRetreiveUpdateDeleteView

urlpatterns = [

    # route to module create view
    path("course/<int:pk>/modules/",ModuleCreateView.as_view()),

    # route to module retrieve,update,delete view
    path("module/<int:pk>/",ModuleRetreiveUpdateDeleteView.as_view()),
]