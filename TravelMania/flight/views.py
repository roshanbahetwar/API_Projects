from django.shortcuts import render
from .models import FlightDetailsModel
from .serializer import FlightDetailsSer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class FlightDetailsView(APIView):
    def get(self,r):
        obj = FlightDetailsModel.objects.all()
        ser = FlightDetailsSer(obj,many=True)
        return Response(ser.data)

    def post(self,r):
        objser = FlightDetailsSer(data=r.data)
        if objser.is_valid():
            objser.save()
            return Response(objser.data,status=status.HTTP_201_CREATED)
        return Response(objser.errors,status=status.HTTP_400_BAD_REQUEST)

class FlightDetailsUpdateDelete(APIView):
    def put(self,r,pk):
        obj = FlightDetailsModel.objects.get(pk=pk)
        objser = FlightDetailsSer(obj, data=r.data)
        if objser.is_valid():
            objser.save()
            return Response(objser.data,status=status.HTTP_201_CREATED)
        return Response(objser.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,r,pk):
        obj = FlightDetailsModel.objetcs.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)