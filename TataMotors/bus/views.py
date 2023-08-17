from django.shortcuts import render,HttpResponseRedirect
from .serializer import BusDetailsSer
from .models import BusDetailsModels
from .form import BusDetailsForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class BusDetailsView(APIView):
    def get(self,r):
        busobj = BusDetailsModels.objects.all()
        serobj = BusDetailsSer(busobj,many=True)
        return Response(serobj.data)

    def post(self,r):
        busser = BusDetailsSer(data= r.data)
        if busser.is_valid():
            busser.save()
            return Response(busser.data,status=status.HTTP_201_CREATED)
        return Response(busser.errors,status=status.HTTP_400_BAD_REQUEST)

'''Additionally form created
instead of admin fill up through 
   form userinterface'''
def busForm(r):
    form = BusDetailsForm()            # from line 20 to 27 for form create additionally instead of admin fillup through form
    if r.method == 'POST':
        form = BusDetailsForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/api/busdetails/')
    return render(r,'details.html',{'form':form})

class BusDetailsUpdateDelete(APIView):
    def put(self,r,pk):
        busobj = BusDetailsModels.objects.get(pk=pk)
        serobj = BusDetailsSer(busobj,data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,r,pk):
        busobj = BusDetailsModels.objects.get(pk=pk)
        busobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)