from django.shortcuts import render, redirect
from main.forms import FormPesanan
from main.models import BuatPesanan
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import BuatPesanan
from django.shortcuts import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

    
@csrf_exempt
def create_pesanan_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        print(data["nama_pesanan"])
        print(data["keterangan"])
        print(data["jumlah_pesanan"])
        user = request.user

        pesanan_baru = BuatPesanan(
            nama_pesanan=data["nama_pesanan"], 
            keterangan=data["keterangan"],
            jumlah_pesanan=data["jumlah_pesanan"],
            user=user
        )

        print("masuk disini")
        pesanan_baru.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)



def buat_pesanan(request):
    form = FormPesanan(request.POST or None)

    if form.is_valid() and request.method == "POST":
        buat_pesanan = form.save(commit=False)
        buat_pesanan.user = request.user
        buat_pesanan.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "buat_pesanan.html", context)

@csrf_exempt
@require_POST
def buat_pesanan_ajax(request):
    nama_pesanan = strip_tags(request.POST.get("nama_pesanan"))
    keterangan = strip_tags(request.POST.get("keterangan"))
    jumlah_pesanan = request.POST.get("jumlah_pesanan")
    user = request.user

    pesanan_baru = BuatPesanan(
        nama_pesanan=nama_pesanan, keterangan=keterangan,
        jumlah_pesanan=jumlah_pesanan,
        user=user
    )
    pesanan_baru.save()

    return HttpResponse(b"CREATED", status=201)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else:
          messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)


@login_required(login_url='/login')
def show_main(request):
    context = {
        'name': request.user.username,
        'service1Name' : 'Mencuci Sepatu',
        'service1Price': 'Rp 75.000',
        'service1Description': 'Kami menggunakan tenaga profesional untuk hasil sepatu yang bersih dan aman',
        'service1Location' : 'Depok, Kukel',
        'service1Duration' : '3 Jam',
        'service2Name' : 'Catering makanan diet',
        'service2Price': 'Rp 399.000',
        'service2Description': 'Kami menggunakan jasa kesehatan dan Chef profesional untuk menghidangkanmu makanan rendah kalori untuk membantu progress dietmu',
        'service2Location' : 'Depok, Kutek',
        'service2Duration' : '1 Minggu(7x3)',
        'service3Name' : 'Kursus anak',
        'service3Price': 'Rp 500.000',
        'service3Description': 'Kami menggunakan tentor profesional untuk mengajari anak SD/SMP/SMA',
        'service3Location' : 'Depok, Margonda',
        'service3Duration' : '1 Minggu (3 Pertemuan)',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
def show_xml(request):
    data = BuatPesanan.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = BuatPesanan.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = BuatPesanan.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = BuatPesanan.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def hapus_semua_pesanan(request):
    if request.method == 'POST':
        BuatPesanan.objects.all().delete()
        return redirect('main:show_main')
    
def edit_pesanan(request, id):
    pesanan = BuatPesanan.objects.get(pk=id)
    form = FormPesanan(request.POST or None, instance=pesanan)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "edit_pesanan.html", context)

def delete_pesanan(request, id):
    pesanan = BuatPesanan.objects.get(pk = id)
    pesanan.delete()
    return HttpResponseRedirect(reverse('main:show_main'))


