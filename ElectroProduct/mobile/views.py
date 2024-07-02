from django.shortcuts import render
from .serializer import MobileDetailsSer
from .models import MobileDetailsModel

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class MobileDetailsView(APIView):
    def get(self,r):
        mobj = MobileDetailsModel.objects.all()
        mser = MobileDetailsSer(mobj,many=True)
        return Response(mser.data)

    def post(self,r):
        objser = MobileDetailsSer(data=r.data)
        if objser.is_valid():
            objser.save()
            return Response(objser.data,status=status.HTTP_201_CREATED)
        return Response(objser.errors,status=status.HTTP_400_BAD_REQUEST)

class MobileDetailsUpdateDelete(APIView):
    def put(self,r,pk):
        mobj = MobileDetailsModel.objects.get(pk=pk)
        mser = MobileDetailsSer(mobj,data=r.data)
        if mser.is_valid():
            mser.save()
            return Response(mser.data,status=status.HTTP_201_CREATED)
        return Response(mser.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,r,pk):
        mobj = MobileDetailsModel.objects.get(pk=pk)
        mobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
