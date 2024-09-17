from django.forms import ModelForm
from main.models import BuatPesanan

class FormPesanan(ModelForm):
    class Meta:
        model = BuatPesanan
        fields = ["nama_pesanan", "keterangan", "jumlah_pesanan"]