from django.shortcuts import render
from .serializer import FeatureDetailsSer
from .models import FeatureDetailsModel

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class FeatureDetailsView(APIView):
    def get(self,r):
        obj = FeatureDetailsModel.objects.all()
        ser = FeatureDetailsSer(obj,many=True)
        return Response(ser.data)

    def post(self,r):
        serobj = FeatureDetailsSer(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status= status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

class FeatureUpdateDelete(APIView):
    def put(self,r,pk):
        obj = FeatureDetailsModel.objects.get(pk=pk)
        serobj = FeatureDetailsSer(obj,data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,r,pk):
        obj = FeatureDetailsModel.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)