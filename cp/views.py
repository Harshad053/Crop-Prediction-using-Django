from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import pickle
from .models import CropData
import os

# Create your views here.
def index(request):
    return render(request,"index.html")

def predict(request):
    if request.method != 'POST':
        return render(request,"index.html")

    if request.method == 'POST':
        N = int(request.POST['N'])
        P = int(request.POST['P'])
        K = int(request.POST['K'])
        temperature=float(request.POST['temperature'])
        humidity=float(request.POST['humidity'])
        ph=float(request.POST['ph'])
        rainfall=float(request.POST['rainfall'])


        with open('static/gnb.pkl','rb')as f:
            mp=pickle.load(f)
        
        pred_value = mp.predict([[N, P,K,temperature,humidity,ph,rainfall]])
        pred_value=str(pred_value[0])
        
        entry=CropData(N=N,P=P,K=K,temperature=temperature,humidity=humidity,ph=ph, rainfall=rainfall,result=pred_value)
        entry.save()

        all_values=CropData.objects.all()
        data={'prediction':pred_value,'all_values':all_values}
        return render(request,'prediction.html', data)


def report(request):
    # if request.method=='POST':

    #     data = request.POST
    #     N = data.get("N")
    #     P = data.get("P")
    #     K = data.get("K")
    #     temperature = data.get("temperature")
    #     humidity = data.get("humidity")
    #     ph = data.get("ph")
    #     rainfall = data.get("rainfall")
    #     prediction = data.get('prediction')

    #     CropData.objects.create(
    #         N =N,
    #         P =P ,
    #         K =K ,
    #         temperature = temperature,
    #         humidity = humidity,
    #         ph = ph,
    #         rainfall = rainfall
    #         )
    #     return redirect('report')

    queryset = CropData.objects.all()
    data = {'data':queryset}

    return render(request,'report.html',data)

