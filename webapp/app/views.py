
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
    if request.method == 'POST':
        selected_date = request.POST['selected_date']
        print(selected_date)
        data = Chripsounder.objects.filter(id=id).values()[0]
        print(data)
        x = os.path.exists('/home/nishayadav/Myprojects/lfm_va')
        if not x:
            filter_ionogram.creating_data_file(data, selected_date)
        lfm_vir = "/home/nishayadav/Myprojects/lfm_va/*"
        files = glob.glob(lfm_vir)
        h5_files = []
        png_files = []
        for file_name in files:
            if file_name.endswith("h5"):
                h5_files.append(file_name)
            else:
                png_files.append(file_name)
        
        # files = [i.split('/')[-1] for i in files]

        # print(h5_files)
        # print(png_files)
        filter_data = []
        for i in h5_files:
            for j in png_files:
                if i.split(".")[0] == j.split(".")[0]:
                    filter_data.append({'h5_file': i.split("/")[-1], 'h5_png_file': j.split("/")[-1]})


        print(filter_data)



        files = enumerate(filter_data)
        base_url = "/home/nishayadav/Myprojects/lfm_va"
        return render(request, 'filter_ionogram.html', {"data": files, "name": data, "base_url": base_url, "selected_date": selected_date})

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



def edit_receiver(request, id):
    data = ReceiverInfos.objects.filter(id = id)
    context = {}
    if request.method == 'POST':
        receiver_name = request.POST['receiver_name']
        receiver_code = request.POST['receiver_code']
        receiver_location = request.POST['receiver_location']
        receiver_lat = request.POST['receiver_lat']
        receiver_long = request.POST['receiver_long']
        
        context.update(
        {
            "receiver_name": receiver_name,
            "receiver_code": receiver_code,
            "receiver_location": receiver_location,
            "receiver_lat": receiver_lat,
            "receiver_long": receiver_long,
        }
        )
        data.update(**context)
        return redirect('receiver-info')
    return render(request, 'edit-receiver.html', {"data": data[0]})
    