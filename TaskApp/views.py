from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from TaskApp.models import TaskDB
from TaskApp.serializers import UserSerializers,TaskSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserRegistrationView(APIView):
    def post(self,request):
        form_data = request.data
        serializer_instance = UserSerializers(data = form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"Message" : "User added sucessfully"})
        else:
            return Response(data = serializer_instance.errors)

    def get(self,request):
        data = User.objects.all()
        serializer_instance = UserSerializers(data,many = True)
        return Response(serializer_instance.data)

class TaskCreateListView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        data = TaskDB.objects.filter(user = request.user)
        serializer_instannce = TaskSerializers(data,many = True)
        return Response(serializer_instannce.data)

    def post(self,request):
        form_data = request.data
        serializer_instance = TaskSerializers(data = form_data)
        if serializer_instance.is_valid():
            serializer_instance.save(user = request.user)
            return Response(data = {
                "Message":"Data Added Successfully",
                "Data": serializer_instance.data
            })
        else:
            return Response(data = serializer_instance.errors)

    

class TaskRetrieveUpdateDeleteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,id):
        form_data = get_object_or_404(TaskDB,id = id)
        if form_data.user == request.user:
            serializer_instance = TaskSerializers(form_data)
            return Response(serializer_instance.data)
        else:
            return Response({"Message":"User id not Valid"})

    def put(self,request,id):
        form_data = request.data
        data_obj = get_object_or_404(TaskDB,id = id)
        if data_obj.user == request.user:
            serializer_instance = TaskSerializers(data = form_data,instance = data_obj)
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(data = {"Message":"Data Added Successfully"})
            else:
                return Response(data = serializer_instance.errors)
        else:
            return Response({"Message":"User id not Valid"})

    def delete(self,request,id):
        data_obj = get_object_or_404(TaskDB,id=id)
        if data_obj.user == request.user:
            data_obj.delete()
            return Response({"Message":"Deletion Successfull"})
        else:
            return Response({"Message":"User id not Valid"})