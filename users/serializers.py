from rest_framework import serializers

from users.models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password_hash")
