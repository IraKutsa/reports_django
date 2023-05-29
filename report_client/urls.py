from django.urls import path
from . import views

urlpatterns = [
    path("reports/", views.ReportsView.as_view()),
    path("reports/<str:id>/", views.GetEditReportsView.as_view()),
    path("users/<int:id>/reports/", views.UserReportsView.as_view()),
    path("projects/<int:id>/reports/", views.ProjectsReportsView.as_view())
]