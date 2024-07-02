from django.shortcuts import render
from .models import JaguarModel
from .serializer import JaguarDetailsSer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class JaguarDetailsView(APIView):
    def get(self,r):
        jlrobj = JaguarModel.objects.all()
        serobj = JaguarDetailsSer(jlrobj,many=True)
        return Response(serobj.data)

    def post(self,r):
        serobj = JaguarDetailsSer(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

class JaguarDetailsUpdateDelete(APIView):
    def put(self,r,pk):
        jlrobj = JaguarModel.objects.get(pk=pk)
        serobj = JaguarDetailsSer(jlrobj,data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,r,pk):
        jlrobj = JaguarModel.objects.get(pk=pk)
        jlrobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)