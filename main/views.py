from django.shortcuts import render, redirect
from main.forms import FormPesanan
from main.models import BuatPesanan
from django.http import HttpResponse
from django.core import serializers

def buat_pesanan(request):
    form = FormPesanan(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "buat_pesanan.html", context)


def show_main(request):
    buat_pesanan = BuatPesanan.objects.all()
    context = {
        
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
        'buat_pesanan': buat_pesanan
    }

    return render(request, "main.html", context)
def show_xml(request):
    data = BuatPesanan.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = BuatPesanan.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = BuatPesanan.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = BuatPesanan.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
# Create your views here.
