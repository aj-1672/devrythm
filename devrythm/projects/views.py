from django.shortcuts import render
from .models import Project


def project_list(request):
    projects = Project.objects.all()  # Make sure this queryset exists
    return render(request, "list.html", {"projects": projects})  # Key must match


def project_detail(request, project_id):
    return render(request, "details.html", {"project_id": project_id})
