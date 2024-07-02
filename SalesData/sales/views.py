from django.shortcuts import render,HttpResponseRedirect
from .serializer import SalesDataSer
from .models import SalesDataModel
from .form import SalesDataForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SalesDataView(APIView):
    def get(self,r):
        obj = SalesDataModel.objects.all()
        ser = SalesDataSer(obj, many=True)
        return Response(ser.data)

    def post(self,r):
        serobj = SalesDataSer(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

def salesForm(r):
    form = SalesDataForm()
    if r.method == 'POST':
        form = SalesDataForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/api/sales_details/')
    return render(r,'sales.html',{'form':form})
