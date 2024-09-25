from django.urls import path
from main.views import show_main, buat_pesanan, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import hapus_pesanan,hapus_semua_pesanan


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('buat_pesanan', buat_pesanan, name='buat_pesanan'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('hapus/<uuid:pesanan_id>/', hapus_pesanan, name='hapus_pesanan'),
    path('hapus_semua/', hapus_semua_pesanan, name='hapus_semua_pesanan'),

]