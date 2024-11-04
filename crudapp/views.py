from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
class StudentData(APIView):

    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            raise Http404

    #CREATE
    def post(self,request):
        ser = StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"success" : True, "data" : ser.data},status=status.HTTP_201_CREATED)
        else:
            return Response({"success" : False, "error" : ser.errors},status=status.HTTP_400_BAD_REQUEST)

    #READ
    def get(self, request):
        sdata = Student.objects.all()
        ser = StudentSerializer(sdata, many=True)
        return Response({"data" : ser.data}, status=status.HTTP_200_OK)

    #UPDATE
    def put(self,request,id, format=None):
        data_obj = Student.objects.get(id=id)
        ser = StudentSerializer(data_obj, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"success" : True, "data" : ser.data},status=status.HTTP_200_OK)
        return Response({"success" : False, "error" : ser.errors}, status=status.HTTP_400_BAD_REQUEST)

    #DELETE
    def delete(self, request, id):
        sdata = self.get_object(id)
        sdata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)