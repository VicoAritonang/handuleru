from django.forms import ModelForm
from main.models import BuatPesanan
from django.utils.html import strip_tags

class FormPesanan(ModelForm):
    class Meta:
        model = BuatPesanan
        fields = ["nama_pesanan", "keterangan", "jumlah_pesanan"]
    def clean_nama_pesanan(self):
        nama_pesanan = self.cleaned_data["nama_pesanan"]
        return strip_tags(nama_pesanan)

    def clean_keterangan(self):
        keterangan = self.cleaned_data["keterangan"]
        return strip_tags(keterangan)