from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers , status
from .models import Student
from rest_framework.views import APIView


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

# Create your views here.

@api_view([ "GET"])
def index(req):
    return Response ("yo yo")



class StudentView(APIView):
    """
    This class handle the CRUD operations for Student
    """
    def get(self, request):
        """
        Handle GET requests to return a list of Student objects
        """
        my_model = Student.objects.all()
        serializer = StudentSerializer(my_model, many=True)
        return Response(serializer.data)


    def post(self, request):
        """
        Handle POST requests to create a new Student object
        """
        # usr =request.user
        # print(usr)
        serializer = StudentSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, pk):
        """
        Handle PUT requests to update an existing Student object
        """
        my_model = Student.objects.get(pk=pk)
        serializer = StudentSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a Student object
        """
        my_model = Student.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
