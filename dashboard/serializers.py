from rest_framework import serializers

from dashboard.models import Dashboard


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        # fields = ("id", "description", "summary", "deadline", "priority", "status", "assignee")
        fields = "__all__"