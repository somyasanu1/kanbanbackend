from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from rest_framework.response import Response

from dashboard.models import Dashboard
from dashboard.serializers import DashboardSerializer
from users.models import User
from users.serializers import UsersSerializer
import copy


def validation(func):
    def inner(self, request, *args, **kwargs):
        try:
            print("REQUEST DATA", request.data)
            data = request.data.dict()
            print(data['amount'])
            return func(self, request, *args, **kwargs)
        except ValueError as e:
            return Response(e, status=200)

    return inner


class ViewAllTask(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DashboardSerializer
    queryset = Dashboard.objects.all()

    def get(self, request, format=None):
        try:
            task = Dashboard.objects.all()
            # user_serializer = UsersSerializer(task.assignee)
            new_serializer = DashboardSerializer(task, many=True)
            response_obj = new_serializer.data
            print(response_obj)
            # response_obj["assignee"] = user_serializer.data['username']
            return Response(response_obj)
        except Exception as e:
            request_obj = {
                "msg": "Some Error Occurred",
                "error": f"The error is {e}"
            }
            return Response(request_obj)


class ViewTask(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DashboardSerializer

    def get(self, request, pk=None, format=None):
        try:
            task = Dashboard.objects.get(pk=pk)
            # user_serializer = UsersSerializer(task.assignee)
            new_serializer = DashboardSerializer(task)
            response_obj = new_serializer.data
            # response_obj["assignee"] = user_serializer.data['username']
            return Response(response_obj)
        except Exception as e:
            request_obj = {
                "msg": "Some Error Occurred",
                "error": f"The error is {e}"
            }
            return Response(request_obj)

    def put(self, request, pk=None, *args, **kwargs):
        try:
            task = Dashboard.objects.get(pk=pk)
            # data = request.data.dict()
            # user_id = data["assignee"]
            # user = User.objects.get(pk=user_id)
            # request_obj = copy.deepcopy(request.data)
            # request_obj["assignee"] = user
            new_task = DashboardSerializer(data=request.data)
            if new_task.is_valid(raise_exception=True):
                new_task.update(task, new_task.data)
                return Response(new_task.data, status=200)
        except Exception as e:
            request_obj = {
                "msg": "Some Error Occurred",
                "error": f"The error is {e}"
            }
            return Response(request_obj, status=400)


class AddTask(generics.CreateAPIView):
    def post(self, request, format=None):
        try:
            new_task = DashboardSerializer(data=request.data)
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


class DeleteTask(generics.RetrieveDestroyAPIView):
    # def get(self, request, pk=None, *args, **kwargs):
    #     try:
    #         task = Dashboard.objects.get(pk=pk)
    #         new_serializer = DashboardSerializer(task)
    #         return Response(new_serializer.data)
    #     except Exception as e:
    #         request_obj = {
    #             "msg": "Some Error Occurred",
    #             "error": f"The error is {e}"
    #         }
    #         return Response(request_obj)

    def delete(self, request, pk=None, *args, **kwargs):
        try:
            Dashboard.objects.filter(pk=pk).delete()
            request_obj = {
                "msg": "Success",
                "result": f"The record with id = {pk} is deleted"
            }
            return Response(request_obj, status=200)
        except Exception as e:
            request_obj = {
                "msg": "Some Error Occurred",
                "error": f"The error is {e}"
            }
            return Response(request_obj, status=400)
