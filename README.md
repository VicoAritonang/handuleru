# Nama : Vico Winner Sebastian Aritonang
# NPM  : 2306219083

## Tautan Web : [http://vico-winner31-handuleru.pbp.cs.ui.ac.id/](http://vico-winner31-handuleru.pbp.cs.ui.ac.id/)


# Jawaban Tugas 2
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Membuat sebuah proyek Django baru.
untuk membuat sebuah proyek Django baru kita perlu menginstal file file yang dibutuhkan. kita bisa membuat requirements.txt berisikan aplikasi atau library yang perlu diinstal untuk membuat website menggunakan Django. setelah semuanya terinstal, kita memerlukan repository git khusus untuk proyek ini. setelah melakukan inisiasi git dengan local, kita dapat menjalankan perintah "django-admin startproject handuleru ."untuk membuat directory project Django didalam directory yang telah kita buat. directory tersebut akan memiliki settings.py untuk pengaturan, kita dapat menambahkan localhost dan 127.0.0.1 kedalam allowed_host agar kita dapat mengakses project kita dari localhost8000. kita dapat Melakukann push directory local kita ke git untuk tahap lebih lanjut.

### Membuat aplikasi dengan nama main pada proyek tersebut.
untuk membuat aplikasi dengan nama main, kita dapat menjalankan perintah (python manage.py startapp main) didalam environment proyek kita. folder main akan tercipta secara otomatis didalam directory local kita. 

## Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
agar aplikasi main dapat dijalankan dalam proyek, kita perlu menambahkan 'main' pada installed_apps di settings.py project directory.

### Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib.
kita dapat membuat folder baru Bernama template pada directory main. dalam folder template, kita dapat membuat sebuah file html Bernama main.html untuk tampilan dari web kita. untuk punya saya, saya membuat variable name, price, description, location, dan duration untuk setiap produk jasa yang saya miliki. saya membangun main.html saya sebaik mungkin lalu menempatkan template_variable pada space tertentu agar bisa mengakses data dari views.py.

### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
pada views.py kita dapat mengimport render terlebih dahulu agar kita bisa menjalankan main.html dari proyek. kita dapat membuat context lalu mengisikan variable template beserta isinya didalamnya. variable template harus memiliki nama yang sama dengan variable template di main.html agar main.html dapat menampilkan nilainya. jika Namanya tidak sama, maka website nantinya tidak akan menampilkan apa apa pada section variable template.

### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
kita perlu membuat urls pada directory proyek dan main agar proyek proyek dapat terhubung dengan app main memalui url tersebut.

### Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
setelah mengerjakan directory local, kita harus melakukan push directory local ke repository lalu melakukan push ke pws dengan cara menjalankan perintah git branch -M main lalu git push pws main:master. setelah itu, pada web pws, project kita akan menampilkan project build, dan apabila sudah success, kita dapat melihat perubahannya di tautan website kita.

### Membuat readme.md
kita dapat membuat readme.md di directory local kita lalu melakukan push ke git. readme.md berisikan text yang ini.


[Bagan](https://drive.google.com/file/d/1mHQBgEP2a1o0k8wHwq9-yfZmMl9pwWt1/view?usp=sharing)

## Jelaskan fungsi git dalam pengembangan perangkat lunak!
Dalam sebuah proyek pengembangan perangkat lunak, kita membutuhkan berbagai keahlian mulai dari membuat design, fungsional, hingga membuat codingannya. Selain itu, setiap bagian dari software tersebut cukup sulit untuk dibuat sehingga kita membutuhkan sebuah tim untuk mengerjakannya. GIt merupakan sebuah Version Control System yang memungkinkan kita mengerjakan sebuah proyek dalam sebuah repository secara bersamaan. Git menyediakan sebuah directory yang dapat diakses oleh sebuah tim dengan berbagai fitur pull, push, clone, dan sebagainya. fitur fitur yang disediakan oleh git sangat berguna untuk proyek pengembangan secara tim. selain itu, kita juga dapat melacak perubahan dan versi setiap project menggunakan git. Git juga memiliki integrasi yang baik dengan banyak software pihak ketiga. oleh karena itu, git sangat berguna dalam pengembangan perangkat lunak secara tim.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Untuk awal pembelajaran, kita menggunakan framework Django karena framework tersebut cukup mudah untuk dipahami untuk pemula. Selain itu, Django project memiliki fitur ORM sehingga kita dapat mengerjakan sebuah project tanpa harus menguasai banyak Bahasa pemrograman. Framework Django juga memiliki struktur dan integrasi yang bagus dan mudah untuk dipahami. Oleh karena itu, Django merupakan framework yang bagus untuk pemula dalam software developing.

## Mengapa model pada Django disebut sebagai ORM?
pada sebuah project Django terdapat file python Bernama models.py
ORM atau Object Relational Mapping adalah sebuah protocol dimana kita bisa menghubungi atau mengakses data base yang menggunakan Bahasa SQL dengan menggunakan Bahasa lain. Models merupakan bagian dari project Django untuk mengatur database dari project. Models pada Django menggunakan python yang mengimport library Django. karena pada Django kita menggunakan Models.py untuk mengakses database, maka hal tersebut sudah termasuk dalam ORM. Bahasa python yang digunakan pada models dapat diartikan sebagai SQL statements pada database. dengan begitu kita relasi antar code dapat dimaksimalkan.

# Jawaban Tugas 3
## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
data delivery adalah proses pengiriman data dari suatu tempat ketempat lain pada suatu sistem, data delivery penting dalam pengimplementasian sebuah platform karena sebuah platform harus memiliki sebuah sistem agar dapat berjalan dengan optimal. data delivery memungkinkan transfer data secara instan dan real time dari database ke template. data delivery memungkinkan kita untuk mengakses data yang kita inginkan lalu menampilkannya. hal ini tentu saja sangat berguna dalam membangun sebuah platform.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Meskipun XML bagus dalam mengolah sebuah data yang kompleks, menurut saya JSON masih lebih baik dibandingkan XML. hal tersebut karena JSON memiliki format dan struktur yang lebih sederhana. kita dapat menuliskan semua objek yang kita butuhkan dengan mudah. selain itu, json lebih mudah dibaca secara langsung karena strukturnya ringkas dan sangat berfokus pada objek dan lebih mudah untuk digunakan. JSON lebih populer dibangdingkan XML karena di era sekarang, lebih banyak web ataupun mobile development yang kompatibel dengan JSON. JSON juga lebih cocok digunakan dalam API modern. oleh karena itu, JSON lebih banyak dipelajari dan lebih populer dibandingkan dengan XML

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
method is_valid() pada form DJango dibutuhkan untuk mengecek input form dari user. saat membuat form, kita menginginkan agar semua field terisi atau diisin dengan format yang sesuai misalnya angka atau huruf agar tidak terjadi error saat pengolahan data. method is.valid() akan mengecek input dari user dan jika semua field telah terisi dengan baik dan benar, maka form.save() atau data akan disimpan. jika tidak sesuai maka akan mengembalikan false

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token adalah sebuah token unik yang dibuat oleh DJango saat membuat form. csrf_token memuat token unik yang digunakan sebagai penanda setiap form yang diakses oleh user. form hanya akan dapat dimasukkan kedalam system jika token yang digunakan sesuai dengan token pada form. jika kita tidak menambahkan csrf_token pada form django, setiap orang dapat memasukkan apapun kedalam form kita tanpa pengawasan. Penyerang dapat memanfaatkan form yang tidak memiliki csrf_token. jika pengguna yang sah login ke dalam aplikasi django, penyerang dapat memanfaatkan pengguna sah tersebut untuk mengunjungi web berbahaya milik penyerang. tanpa csrf_token, penyerang dapat mengirimkan permintaan POST ke aplikasi django. karena form tersebut dari pengguna yang sah, sistem akan menerima FORM tersebut tanpa menyadari itu adalah serangan.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### membuat input form
input form yang akan kita buat pastinya akan memiliki template berupa html. untuk itu, kita harus membuat kerangka umum untuk setiap file html yang kita buat. kita dapat membuat file base.html yang mendefinisikan {%block%} agar dapat digunakan oleh setiap file html pada system. setelah itu, kita mengakses base.html tersebut dan mengimplementasikan nya ke semua file html kita.kita dapat membuat template untuk form dan memasukkannya pada directory template pada aplikasi. selanjutnya kita membuat forms.py di directory aplikasi. forms.py ini akan mengambil data variabel dari models lalu kita dapat menentukan variabel untuk setiap field isian dari user. lalu kita dapat mengakses views dan mengimport redirect. setelah itu kita membuat fungsional dari form pada views. views akan mengakses form dan merender template form. setelah itu kita bisa menambahkan path pada urls aplikasi untuk mengakses form tersebut. setelah itu, karena kita membuat form pada template yang berbeda, kita harus membuat link atau button pada main.html agar bisa mengakses template form. field isian akan ada pada template form.

### Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
untuk membuat fungsi vews yang baru, kita dapat mengimport uuid terlebih dahulu pada models, lalu kita dapat membuat variable bersangkutan dan melakukan migrate models. selanjutnya kita mengimport http response dan serializers pada views.py. setelah itu kita dapat membuat show_xml dan show_json dengan meminta parameter request. show_xml dan show_json akan membuat object data dan akan berisi semua data object yang diisi menggunakan form. show_xml dan show_json akan menampilkan semua data object. lalu kita dapat membuat show xml dan json by id. kita dapat membuat fungsi tersebut dengan parameter request dan id. fungsi tersebut akan mengembalikan object dengan id yang sesuai.

### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
kita dapat membuat routing URL dengan membuka urls.py pada directory aplikasi. kita bisa mengimport keempat fungsi tadi dari views lalu membuat path url untuk fungsi tersebut dengan mengetikkan id nya. saat kita mengakses website kita, kita bisa mengakses keempat fungsi show tersebut menggunakan url browser.

[link screenshot Postman](https://drive.google.com/drive/folders/1NfOiWwGFhluqH-mfbYCocuXxgMls9yD8?usp=sharing)

# Jawaban Tugas 4
## Apa perbedaan antara HttpResponseRedirect() dan redirect()
dalam sebuah proyek django kita dapat mengimport HttpResponseRedirect dan redirect. kedua fungsi ini memiliki tujuan yang sama yaitu mengarahkan pengguna ke halaman tertentu. dalam tugas saya, saya menggunakannya untuk mengalihkan pengguna dari halaman login ke halaman utama, dan halaman utama ke halaman login melalui log out. akan tetapi, fungsi HttpResponseRedirect memiliki lebih banyak control terhadap cookie dibandingkan dengan redirect. menggunakan HttpResponseRedirect, kita dapat mendapatkan data cookie seperti waktu, durasi, path, dan sebagainya. fungsi redirect tidak dapat melakukan hal tersebut secara langsung sehingga kita harus mengatur cookie secara terpisah. akan tetapi redirect memiliki penulisan yang lebih ringkas dibandingkan httpresponseredirect. oleh karena itu kita dapat memilih penggunaannya sesuai dengan kebutuhan kita.

## Jelaskan cara kerja penghubungan model Product dengan User!
pada sebuah proyek django, kita dapat mengimpor user dari library dan mendefinisikannya pada models.py. user dalam proyek django dapat dibuat ketika kita memiliki fitur login dan register pada proyek django kita. kita dapat membuat sebuah form untuk login lalu menyimpannya ke database kita sebagai user. kita dapat mengambil data user dari model setelah melakukan migrasi model. dengan begitu, kita dapat menyesuaikan data di views berdasarkan user secara spesifik. dalam tugas saya, saya dapat mengambil username dari user kedalam views lalu menampilkannya pada template main.

## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Saat membuat sebuah proyek django, kita dihadapkan dengan autentifikasi dan autorisasi. Autentifikasi adalah proses dimana website atau proyek django yang kita buat mengecek apakah kita adalah user yang tepat/terdaftar atau tidak. autentifikasi terjadi saat kita melakukan login pada form login. views.py pada proyek django akan mengambil kelas AuthenticationForm dan menggunakan parameter login untuk mengecek apakah pengguna sah atau tidak untuk login. sedangkan autorisasi adalah sebuah proses dimana sistema akan mengecek apakah kita sah untuk mengakses resource tertentu atau melakukan kegiatan tertentu pada sistem. autorisasi digunakan untuk membatasi hak pengguna untuk mengakses path atau halaman tertentu pada proyek. kita dapat menggunakan syntax seperti 
@login_require(login_url='/ login') diatas fungsi yang ditentukan untuk autorisasi pada tugas saya.

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
django dapat mengingat pengguna yang telah login dengan mengimpor login dari library django.contrib.auth. Django akan menyimpan semua ID sesi dari setiap pengguna yang melakukan register dan login. setiap sesi login setiap user yang terdaftar akan disimpan dalam database. django dapat menyimpan user login beserta file dan data lain kedalam database. setelah login django dapat mengirimkan cookie ke browser dan bisa mendapatkan beberapa informasi tentang pengguna seperti tema, bahasa, perilaku pengguna di browser, dan sebagainya. cookie juga dapat menjaga user yang login tetap terautorisasi saat ingin melakukan action di dalam website. dengan begitu, user tidak perlu login berulang ulang saat ingin melakukan sesuatu. sebagian besar cookie aman untuk digunakan dalam website. akan tetapi, kita harus membatasi masa hidup cookie agar terhindar dari serangan terutama jika cookie berisi informasi sensitif pengguna. selain itu, kita dapat menggunakan secure dan samesite cookies untuk mencegah beberapa jenis serangan.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
untuk mengimplementasikan fungsi registrasi, login, dan logout, kita dapat terlebih dahulu membuat template form register dan form login pada directory main/template. lalu kita dapat membuat fungsi register pada views.py. fungsi register akan menciptakan form register lalu meminta isian form. jika isian form register valid, akun akan ditambahkan ke database. lalu kita dapat membuat fungsi login pada views.py. fungsi login tersebut akan mengakses kelas AuthenticationForm untuk mengecek apakah user dan pasword sesuai dan terdaftar di database atau tidak. jika login berhasil, pengguna akan dialihkan ke halaman utama. untuk fungsi logout, kita dapat membuat fungsi logout di views.py. kita dapat memanggil method logout dengan parameter request. dengan begitu kita akan mengeluarkan akun yang sedang login di website. setelah itu, kita dapat menyesuaikan tombol pada main.html terhadap fungsi fungsi yang baru kita buat. selanjutnya kita harus menambahkan path untuk setiap fungsi pada urls.py. setelah semua nya telah terintegrasi, kita dapat melakukan registrasi dan login untuk masuk ke aplikasi sebelumnya lalu logout untuk keluar.

###  Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
kita dapat membuat akun  pengguna dengan mengaktifkan server dan mengakses localhost. kita dapat membuat akun pengguna secara langsung dengan mengisi registration form. untuk tahap ini saya membuat akun untuk user01, user02, dan user03 dengan password yang berbeda beda. 

### Menghubungkan model Product dengan User.
untuk menghubungkan model product dengan user, kita dapat mengimpor user dari django pada models.py terlebih dahulu. selanjutnya kita harus mendefinisikan variabel user pada models dengan user = models.ForeignKey(User, on_delete=models.CASCADE). setelah itu kita dapat mengakses user ke dalam views.py dan dapat mengambil informasi dari setiap user untuk nantinya dimasukkan kedalam template. kita dapat menyesuaikan user pada views dengan melakukan request terhadap user untuk mengakses informasi tentang user. setelah itu kita dapat melakukan migrasi model pada terminal. setelah itu kita dapat melakukan penyesuaian pada settings.py untuk mengambil data dari environtment variabel bernama production dengan mengimport OS.

## Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

untuk mengakses informasi pengguna yang sedang login, kita dapat melakukan request dan memasukkannya dalam code yang kita mau. contohnya dalam tugas saya, saya mengakses nya dari context pada show_main yang meminta parameter request. setelah menginisiasi user pada models pada tahap sebelumnya, kita dapat mengakses informasi user dari views.py. jika kita ingin mengakses username, kita dapat menggunakan syntax reques.user.username. untuk mengambil data cookie kita dapat menggunakan request.COOKIES['last login'] untuk mendapatkan data login dari COOKIES. request tersebut akan mengembalikan informasi tentang user yang sedang login karena parameter request yang dimiliki oleh show_main berasal dari login user.

# Jawaban Tugas 5

## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
dalam CSS selektor pengambilan CSS Selector akan memprioritaskan ID selector seperti #header sebagai prioritas pertama dalam me run sebuah file, setelah itu CSS selector akan memilih class atau pseudo class sebagai prioritas kedua. untuk prioritas ketiga, CSS selector akan mengambil element / pseudo element seperti div. jika Selector menemukan spesifikasi yang sama dalam file, selector akan mengutamakan spesifikasi yang dideklarasikan paling akhir (Cascading). selain itu selector juga memiliki aturan !important yang akan didahulukan dari semua spesifikasi. jika terdapat lebih dari 1 important maka akan mengikuti aturan cascading juga.

## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
responsice design sangat penting dalam pengembangan aplikasi web karena pengguna bisa saja mengakses aplikasi dari desktop maupun mobil, horizontal ataupun vertikal. responsive design akan membuat aplikasi fit in pada setiap perangkat pengguna sehingga akna meningkatkan user experience. responsive design juga membuat pengguna dapat lebih interaktif dengan aplikasi karena pengguna dapat melakukan zoom, pencarian dan sebagainya dengan baik sehingga dapat meningkatkan pengguna juga. aplikasi yang belum menerapkan responsive design biasanya aplikasi tugas anak sekolah ataupun aplikasi lama pemerintahan. aplikasi yang sudah menerapkannya seperti instagram dan kebanyakan medsos lainnya.


## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
dalam CSS margin, border, dan padding adalah cara yang dapat digunakan untuk mengatur sebuah blok pada file html. margin mengatur bagian paling luar dari sebuah blok. margin dapat digunakan untuk hal seperti mengatur area blok. setelah itu ada border. border adalah bagian terluar dari blok sebelum margin. blok biasanya digunakan untuk mengatur ketebalan warna antar margin dengan tulisan didalamnya. selanjutnya adalah padding, padding digunakan untuk memberikan area atau latar belakang tempat kita memasukkan teks atau gambar. padding adalah area isi konten dalam sebuah blok.
untuk memanggil margin kita dapat menggunakan
'''
    margin : 50 px; 
'''
artinya bagian kiri kanan atas bawah margin berjarak 50 px

untuk memanggil border kita dapat menggunakan
'''
border : 1px solid #000;
'''
artinya border memiliki ketebalan 1px dan warna #000. 

untuk memanggil padding kita dapat menggunakan
'''
 padding: 10px;
'''
artinya konten berada pada jarak 10 px dari border

##  Jelaskan konsep flex box dan grid layout beserta kegunaannya!
flexbox dan grid layout merupakan cara untuk menyusun sebuah layout dalam CSS. flexbox akan menyusun elemen dalam satu dimensi / arah / 1D. dengan flex box dapat menyusun konten dari css secara vertikal dari atas kebawah ataupun secara horizontal dari kiri ke kanan. dengan flex box setiap kita menambahkan elemen dalam css, dia akan disusun secara horizontal atau vertikal. grid layout adalah cara menyusun elemen dari css dalam 2 dimensi. kita dapat membuat display kita seperti matrix yang memiliki kolom dan baris. dengan grid layout, kita dapat menyusun konten kita di area yang kita mau hanya dengan memberikan informasi mengenai baris dan kolom nya saja. flex box cocok untuk menyusun suatu hal yang dapat bertambah terus menerus seperti tambah pesanan atau semacamnya sedangkan grid cocok untuk menyusun sebuah display dengan design yang sudah ditetapkan 

## Jelaskan checklist
### Implementasikan fungsi untuk menghapus dan mengedit product.
untuk membuat fungsi mengedit produk kita bisa membuat file html edit_produk.html untuk template dari fungsi edit_produk. lalu kita dapat membuat fungsi edit produk dengan membuat sebuah fungsi yang meminta parameter dan id lalu men save form dengan id tersebut dan mereturn nya kembali. untuk menghapus pesanan kita dapat membuat fungsi hapus_pesanan di views.py lalu menggunakan method .delete() untuk menghapus pesanan dengan id tertentu. tambahkan tombol di main.html lalu tambahkan path di urls.py dengan meminta uuid dari setiap pesanan

## Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework
saya menggunakan css tailwind untuk mendesifn file html saya seperti buat_pesanan, edit_pesanan, main.html, hingga register akun. saya menggunakan css sederhana untuk membuat container dan menyusun nya secara sederhana dibagian tengah. untuk main.html bagian menyusun kartu, saya menggunakan grid karena menurut saya lebih cantik. selanjutnya saya membuat card_pesanan.html sebagai template dari pesanan yang telah dibuat. saya mengatur margin, padding, dan border sedemikian rupa agar bisa menampilkan web dengan baik.

## Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
untuk membuat sebuah navbar yang dapat beradaptasi dengan ukuran device khususnya mobile dan desktop, saya membuat penyesuaian css untuk keduanya. saya juga hanya menampilkan home, kategori, produk, dan keranjang sebagai tulisan tanpa fungsi tombol karena saya belum memikirkan langkah selanjutnya.


# Jawaban Tugas 6
## Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
Dalam pengembangan aplikasi web, penggunaan Javascript dapat membuat web menjadi
lebih interaktif. Javascript dapat memberikan fungsional bagi sebuah web seperti saat di klik
dan sebagainya. Javascript juga dapat membuat respon web lebih cepat karena fitur
asinkronus atau AJAX. Dengan AJAX, user tidak perlu selalu meminta request dari server
tetapi bisa mendapatkan response yang diinginkan secara asinkronus melalui javascript yang
tertanam pada web untuk beberapa fungsional. Dengan begitu, web dapat dijalankan dengan
response yang lebih cepat sehingga dapat meningkatkan pengalaman pengguna. Javascript
juga dapat meningkatkan interaktivitas pengguna. Pengguna dapat melakukan berbagai action
dan mendapatkan response secara cepat dari website. Javascript juga memungkinkan
pengguna mengakses web multiplatform seperti mobile, desktop dan sebagainya.

## Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan
terjadi jika kita tidak menggunakan await?
Await adalah keyword pada javascript yang digunakan untuk mengatasi operasi asinkronus.
Await akan membuat program berhenti sejenak sampai operasi yang dikenakan await selesai
apapun hasilnya. Penggunaan await saat menggunakan fetch memungkinkan kita untuk
menghentikan program sejenak hingga fetch() selesai. Fungsinya adalah saat menggunakan
operasi asinkronus, kita dapat menunggu operasi asinkronus tersebut selesai lalu
menggunakan hasil data nya untuk kode program selanjutnya. Jika kita tidak menggunakan
await, program akan langsung menjalankan kode selanjutnya yang jika meminta data dari
proses asinkronus akan menyebabkan error atau data yang digunakan bukanlah data akhir
yang diinginkan (dari asinkronus proses) oleh karena itu kita perlu menggunakan await
karena pada dasarnya proses asinkronus dapat berjalan bersamaan dengan program utama
sehingga kita memerlukan await untuk menghubungkannya.

## Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan
untuk AJAX POST?
Saat kita ingin mengirimkan sebuah request seperti POST ke server, Django akan memeriksa
csrf token yang digunakan pada request dan akan mengembalikan error jika csrf nya tidak
tepat. Kita menggunakan csrf_extempt pada view untuk fungsi AJAXPOST agar fungsi
tersebut dapat berjalan dengan baik setelah user melakukan login. Jika kita tidak
menggunakan csrf_extempt maka Django akan mengembalikan error setiap kita ingin
mengakses fungsi AJAXPOST. Data yang kita isikan secara asinkronus tidak akan sampai ke
server. Sedangkan jika kita menggunakan csrf_extempt, kita akan memberikan autentifikasi
pada user logged in sehingga ia bisa melakukan request POST pada fungsi AJAXPOST dan
sampai ke server.

## Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang
(backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Pembersihan data input dapat dilakukan pada frontend seperti validasi input dan sebagainya.
Akan tetapi, input yang masuk di frontend dapat dilewati menggunakan javascript sehingga
akan berbahaya jika masuk ke server dan membuat request. Pada tutorial minggu ini, kita bisa
memanggil alert dengan memasukkan javascript di kolom input. Pembersihan data yang
dilakukan di backend seperti yang kita lakukan pada tutorial akan memeriksa input dari
pengguna dan menghapus tag tag yang memungkinkan input tersebut dapat dijalankan
sebagai javascript atau semacamnya. Dengan pembersihan data pada backend, kita dapat
menghindarkan proyek kita dari Cross-Site Scripting.

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

pertama kita perlu membuat fungsi buat_pesanan_ajax di views.py. buat_pesanan_ajax akan menggunakan parameter request dan melakukan request post untuk nama_pesanan, keterangan, dan jumlah pesanan. setelah itu kita membuat sebuah objek BuatPesanan dan mensave nya ke user yang sedang login dengan request.user. fungsi ini menggunakan dekorator @csrd_exempt untuk autentifikasinya. fungsi ini akan mengembalikan httpResponse() untuk membuat pesanan baru. setelah kita membuat fungsi ini, kita perlu menambahkan path nya ke urls.py agar dapat diakses di peramban. setelah itu, kita dapat menghapus pesanan di show_main pada views.py karena kita akan mengolahnya di templates. kita juga dapat menghapus bagian untuk mencetak pesanan di main.py dan menggantinya dengan kartu pesanan saja. setelah itu, kita perlu menambahkan javascript di main.html untuk ajaxnya. kita dapat membuat fungsi asinkronus getPesanan yang menggunakan fetch untuk mengkonversi hasil response nya menjadi json yang dapat ditampilkan. karena fungsi ajax ini asinkronus, kita perlu membuat sebuah fungsi refreshPesanan untuk selalu memperbarui data yang ada pada server untuk user. fungsi ini juga mengembalikan tidak ada pesanan jika pesanan kosong, dan memungkinkan kita untuk meletakkan fungsi hapus dan edit pesanan. dengan begitu data pesanan akan selalu diperbarui dengan data dari sumber data secara asinkronus. selanjutnya kita perlu membuat form ajax untuk menerima input pesanan. kita dapat membuat modal pop up web untuk form isiannya. lalu kita perlu membuat fungsi buatPesanan juga di javascript yang terhubung ke buat_pesanan_ajax di views.py. fungsi ini akan menggunakan modal sebagai form dan akan membuat object BuatPesanan untuk menambahkan pesanan. untuk menjaga keamanan dari serangan Cross Site Scripting, kita dapat mengimport strip_tags terlebih dahulu lalu menggunakannya pada fungsi buat_pesanan_ajax. setelah itu kita dapat menambahkan fungsi pembersihan untuk nama_pesanan dan keterangan di form.py menggunakan strip_tags juga. pembersihan ini akan menghapus tag tag pada input berupa script yang dimasukkan melalui form isian. lalu kita dapat menggunakan method sanitaze dari DOMPurify pada javascript untuk menghapus atau memodifikasi elemen elemen berbahaya pada html.


