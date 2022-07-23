from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response

from users.models import User
from users.serializers import UsersSerializer


class ViewUsers(generics.ListCreateAPIView):
    serializer_class = UsersSerializer
    queryset = User.objects.all()

    def get(self, request, pk=None, format =None):
        if pk:
            try:
                users = User.objects.get(pk=pk)
                new_serializer = UsersSerializer(users)
                return Response(new_serializer.data)
            except Exception as e:
                request_obj = {
                    "msg": "Some Error Occurred",
                    "error": f"The error is {e}"
                }
            return Response(request_obj)
        try:
            users = User.objects.all()
            new_serializer = UsersSerializer(users, many=True)
            return Response(new_serializer.data)
        except Exception as e:
            request_obj = {
                "msg": "Some Error Occurred",
                "error": f"The error is {e}"
            }
            return Response(request_obj)

    def post(self, request, format=None):
        try:
            new_task = UsersSerializer(data=request.data)
            print(new_task)
            if new_task.is_valid(raise_exception=True):
                new_task.save()
                return Response(new_task.data, status=200)
        except Exception as e:
            request_obj = {
                "msg": "Some Error Occurred",
                "error": f"The error is {e}"
            }
            return Response(request_obj, status=400)

