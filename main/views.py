from django.shortcuts import render
def show_main(request):
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
        'service4Name' : 'Antar Jemput Kampus',
        'service4Price': 'Rp 800.000',
        'service4Description': 'Menggunakan jasa driver disiplin dan terpercaya untuk mengantar dan menjemputmu dari kampus ke rumaha',
        'service4Location' : 'Depok, pondok cina',
        'service4Duration' : '1 Bulan (2 kali sehari)',
    }

    return render(request, "main.html", context)
# Create your views here.
