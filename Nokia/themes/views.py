from django.shortcuts import render
from .serializer import ThemesDetailsSer
from .models import ThemesDetailsModels

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ThemesDetailsView(APIView):
    def get(self,r):
        themesobj = ThemesDetailsModels.objects.all()
        objser = ThemesDetailsSer(themesobj,many=True)
        return Response(objser.data)
    def post(self,r):
        serobj = ThemesDetailsSer(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data, status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

class ThemesDetailsUpdateDelete(APIView):
    def put(self,r,pk):
        tobj = ThemesDetailsModels.objects.get(pk=pk)
        serobj = ThemesDetailsSer(tobj,data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,r,pk):
        tdobj = ThemesDetailsModels.objects.get(pk=pk)
        tdobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

