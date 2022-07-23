from django.db import models


# Create your models here.
from users.models import User


class Dashboard(models.Model):
    id = models.AutoField(db_column="id", primary_key=True)
    description = models.TextField(db_column="description", blank=False, null=False)
    summary = models.TextField(db_column="summary", blank=False, null=False)
    deadline = models.TextField(db_column="deadline", blank=False, null=False)
    priority = models.CharField(max_length=399, db_column="priority", blank=False, null=False)
    status = models.CharField(max_length=399, db_column="status", blank=False, null=False)
    assignee = models.IntegerField(db_column="assignee", blank=False, null=False)

    class Meta:
        db_table = "tasks"
