
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Chripsounder, ReceiverInfos, DirectoryInfos
from . import filter_ionogram
from django.contrib import messages
import psycopg2
import glob

# Create your views here.

def homepage(request):
    data = Chripsounder.objects.all()
    return render(request, 'index.html', {"data": data})


def filter_ionograms(request, id):
    data = Chripsounder.objects.filter(id=id).values()[0]
    print(data)
    x = os.path.exists('/home/nishayadav/Myprojects/lfm_va')
    if not x:
        filter_ionogram.creating_data_file(data=data)
    lfm_vir = "/home/nishayadav/Myprojects/lfm_va/*"
    files = glob.glob(lfm_vir)
    files = [i.split('/')[-1] for i in files]
    files = enumerate(files)
    return render(request, 'filter_ionogram.html', {"data": files, "name": data})

def edit_transmitter(request, id):
    data = Chripsounder.objects.filter(id = id)
    context = {}
    if request.method == 'POST':
        name_of_transmitter = request.POST['transmitter_name']
        tx_code = request.POST['tx_code']
        lat = request.POST['lat']
        long = request.POST['long']
        ground_range = request.POST['ground_range']
        first_hop_range_one = request.POST['first_hop_range_one']
        first_hop_range_two = request.POST['first_hop_range_two']
        chriprate = request.POST['chrip_rate']
        second_hop_range_one = request.POST['second_hop_range_one']
        second_hop_range_two = request.POST['second_hop_range_two']
        context.update(
        {
            "name_of_transmitter": name_of_transmitter,
            "tx_code": tx_code,
            "lat": lat,
            "longitude": long,
            "range_zero":ground_range,
            "chriprate": chriprate,
            "first_hop_range_one": first_hop_range_one,
            "first_hop_range_two": first_hop_range_two,
            "second_hop_range_one": second_hop_range_one,
            "second_hop_range_two":second_hop_range_two,
        }
        )
        data.update(**context)
        return redirect('homepage')
    return render(request, 'edit.html', {"data": data[0]})



def receiver_info(request):
    data = ReceiverInfos.objects.all()
    return render(request, 'admin.html', {'data': data})



def filter_ionogramss(request):
    pass