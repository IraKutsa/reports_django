from django.urls import path
from . import views

urlpatterns = [
    path("reports/", views.ReportsView.as_view()),
    path("reports/<str:id>", views.EditReportsView.as_view()),
    path("users/<str:id>/reports/", views.UserReportsView.as_view()),
    path("projects/<str:id>/reports/", views.ProjectsReportsView.as_view())
]