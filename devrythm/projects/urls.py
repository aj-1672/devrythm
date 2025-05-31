from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    path("", views.project_list, name="project_list"),  # List all projects
    path(
        "<int:project_id>/", views.project_detail, name="project_detail"
    ),  # Single project detail
]
