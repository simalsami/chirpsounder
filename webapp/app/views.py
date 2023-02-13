from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Chripsounder, ReceiverInfos, DirectoryInfos
from . import filter_ionogram
from django.contrib import messages
import psycopg2
import glob
from datetime import datetime, timedelta, timezone
from .plot_ionograms import create_plot_ionograms

# Create your views here.

def homepage(request):
    data = Chripsounder.objects.all()
    return render(request, 'index.html', {"data": data})



def view_ionograms(request, filename):
    """
    Functions to vew ionograms

    """

    lfm_vir = "/home/nishayadav/chirpsounder2_django/chirpsounder/webapp/app/static/lfm_va/*"
    files = glob.glob(lfm_vir)
    h5_files = []
    png_files = []
    for file_name in files:
        if file_name.endswith("h5"):
            h5_files.append(file_name)
        else:
            png_files.append(file_name.split("/")[-1])
    

    
    filter_data = []
    for i in h5_files:
        png_file = i.split("/")[-1]       

        if f'{png_file[0: -2]}png' in png_files:
            filter_data.append(f'{png_file[0: -2]}png')

    

    for_previous = []
    for_next = []

    index = filter_data.index(filename)
    for_previous = filter_data[0: index]
    for_next = filter_data[index+1:]

    print(len(for_next))
    print(len(for_previous))

    return render(request, 'view-ionograms.html', {"filename": filename, "for_previous": for_previous, "for_next": for_next})


def timestamp_to_datetime(timestamp):
    """
    This function is used to convert the timestamp to readable date time. 


    """
    print("timestamp", timestamp)
    timestamp = int(timestamp)
    # print(timestamp)
    dt = datetime.utcfromtimestamp(timestamp).replace(tzinfo=timezone.utc) + timedelta(hours=5)
    dt = dt.strftime("%Y-%m-%d %I:%M:%S %p")
    return dt


def filter_ionograms(request, id):
    data = Chripsounder.objects.filter(id=id).values()[0]
    print(data)
    if request.method == 'POST':
        selected_date = request.POST['selected_date']
        print(selected_date)
        
        x = os.path.exists('/home/nishayadav/Myprojects/lfm_va')
        if not x:
            filter_ionogram.creating_data_file(data, selected_date)
    lfm_vir = "/home/nishayadav/chirpsounder2_django/chirpsounder/webapp/app/static/lfm_va/*"
    files = glob.glob(lfm_vir)
    h5_files = []
    png_files = []
    for file_name in files:
        if file_name.endswith("h5"):
            h5_files.append(file_name)
        else:
            png_files.append(file_name.split("/")[-1])
    
    # files = [i.split('/')[-1] for i in files]

    # print(h5_files)
    print(png_files)
    filter_data = []
    for i in h5_files:
        png_file = i.split("/")[-1]
        # print(f'{png_file[0: -2]}png')

        if f'{png_file[0: -2]}png' in png_files:
            filter_data.append(
            {'h5_file': i.split("/")[-1], 
            'h5_png_file': f'{png_file[0: -2]}png',
            'selected_date': timestamp_to_datetime(i.split("/")[-1].split("-")[2].split(".")[0])
            }
            )
        else:
            filter_data.append(
            {'h5_file': i.split("/")[-1], 
            'selected_date': timestamp_to_datetime(i.split("/")[-1].split("-")[2].split(".")[0])
            }
            )

    files = enumerate(filter_data)
    base_url = "/home/nishayadav/Myprojects/lfm_va"
    return render(request, 'filter_ionogram.html', {"data": files, "name": data, "base_url": base_url})

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
    

def create_ionograms(request, filename):
    print(filename)
    create_plot_ionograms(filename)
    return redirect('/filter-ionograms/3')

def get_folder_name(path):
    return {"folder_name": path.split("/")[-1]}

rootdir = '/media/nishayadav/Seagate Backup Plus Drive/chirp/*'
def unfiltered_ionograms(request):
    lst = glob.glob(rootdir)
    lst = list(map(get_folder_name, lst))
    print(lst)


    # user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(lst, 40)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    print(users)
    return render(request, 'all-ionograms.html', {"users": users})

def view_filtered_ionograms(request):
    lst = glob.glob(rootdir)
    lst = list(map(get_folder_name, lst))
    print(lst)


    # user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(lst, 40)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    print(users)
    return render(request, 'view-filtered_ionogram.html', {"users": users})

# def remove_path_from_ionograms(path):
#     return {"folder_name": path.split("/")[-1]}

def view_unfiltered_ionograms(request, folder_name):
    rootdir = '/media/nishayadav/Seagate Backup Plus Drive/chirp'
    png_files = []
    lst = glob.glob(f"{rootdir}/{folder_name}/lfm*.png")



    files = glob.glob(f"{rootdir}/{folder_name}/*")
    h5_files = []
    png_files = []
    for file_name in files:
        if file_name.endswith("h5"):
            h5_files.append(file_name)
        else:
            png_files.append(file_name.split("/")[-1])
    
    # files = [i.split('/')[-1] for i in files]

    # print(h5_files)
    print(png_files)
    filter_data = []
    for i in h5_files:
        png_file = i.split("/")[-1]
        # print(f'{png_file[0: -2]}png')

        if f'{png_file[0: -2]}png' in png_files:
            filter_data.append(
            {'h5_file': i.split("/")[-1], 
            'h5_png_file': f'{png_file[0: -2]}png',
            'selected_date': folder_name
            }
            )
        else:
            filter_data.append(
            {'h5_file': i.split("/")[-1], 
            'selected_date': folder_name
            }
            )

    files = enumerate(filter_data)
    base_url = "/home/nishayadav/Myprojects/lfm_va"

    

    # for i in lst:
    #     png_files.append(f"{folder_name}/{i.split('/')[-1]}")

    # print(png_files)

    return render(request, 'view-unfiltered_ionograms.html', {"data": files, "base_url": base_url, 'selected_date': folder_name})

