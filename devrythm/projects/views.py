from django.shortcuts import render


def project_list(request):
    return render(request, "list.html")  # You'll create this template later


def project_detail(request, project_id):
    return render(request, "details.html", {"project_id": project_id})
