import uuid
from django.db import models
from django.contrib.auth.models import User

class BuatPesanan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    nama_pesanan = models.CharField(max_length=255)
    waktu_pemesanan = models.DateField(auto_now_add=True)
    keterangan = models.TextField()
    jumlah_pesanan = models.IntegerField()

    @property
    def pesanan_banyak(self):
        return self.jumlah_pesanan > 5