from django.shortcuts import render
from .models import CarDetailsModel
from .serializer import CarDetailsSer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class CarDetailsView(APIView):
    def get(self,r):
        car_obj = CarDetailsModel.objects.all()
        serobj = CarDetailsSer(car_obj,many=True)
        return Response(serobj.data)

    def post(self,r):
        serobj = CarDetailsSer(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

class CarDetailsUpdateDelete(APIView):
    def put(self,r,pk):
        carobj = CarDetailsModel.objects.get(pk=pk)
        serobj = CarDetailsSer(carobj,data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status= status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,r,pk):
        carobj = CarDetailsModel.objects.get(pk=pk)
        carobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)