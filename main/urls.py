from django.urls import path
from main.views import show_main, buat_pesanan, show_xml, show_json, show_xml_by_id, show_json_by_id, buat_pesanan_ajax
from main.views import register
from main.views import login_user, delete_pesanan
from main.views import logout_user, edit_pesanan
from main.views import hapus_semua_pesanan, create_pesanan_flutter


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
    path('hapus_semua/', hapus_semua_pesanan, name='hapus_semua_pesanan'),
    path('edit-pesanan/<uuid:id>', edit_pesanan, name='edit_pesanan'),
    path('delete/<uuid:id>', delete_pesanan, name='delete_pesanan'),
    path('buat-pesanan-ajax', buat_pesanan_ajax, name='buat_pesanan_ajax'),
    path('create-flutter/', create_pesanan_flutter, name='create_pesanan_flutter'),

]