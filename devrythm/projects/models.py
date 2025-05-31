from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)  # Project title
    description = models.TextField(blank=True)  # Optional description
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set creation time

    def __str__(self):
        return self.name  # How projects appear in admin
