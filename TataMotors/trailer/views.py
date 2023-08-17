from django.shortcuts import render
from .serializer import TrailerDetailsSer
from .models import TrailerDetailsModel

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class TrailerDetailsView(APIView):
    def get(self,r):
        tobj = TrailerDetailsModel.objects.all()
        serobj = TrailerDetailsSer(tobj,many=True)
        return Response(serobj.data)

    def post(self,r):
        sobj = TrailerDetailsSer(data=r.data)
        if sobj.is_valid():
            sobj.save()
            return Response(sobj.data,status=status.HTTP_201_CREATED)
        return Response(sobj.errors,status=status.HTTP_400_BAD_REQUEST)

class TrailerDetailsUpdateDelete(APIView):
    def put(self,r,pk):
        tobj = TrailerDetailsModel.objects.get(pk=pk)
        sobj = TrailerDetailsSer(tobj,data=r.data)
        if sobj.is_valid():
            sobj.save()
            return Response(sobj.data,status=status.HTTP_201_CREATED)
        return Response(sobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,r,pk):
        trobj = TrailerDetailsModel.objects.get(pk=pk)
        trobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)