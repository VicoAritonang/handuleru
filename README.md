Nama : Vico Winner Sebastian Aritonang
NPM  : 2306219083

Tautan Web : http://vico-winner31-handuleru.pbp.cs.ui.ac.id/

===================================================================
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Membuat sebuah proyek Django baru.
untuk membuat sebuah proyek Django baru kita perlu menginstal file file yang dibutuhkan. kita bisa membuat requirements.txt berisikan aplikasi atau library yang perlu diinstal untuk membuat website menggunakan Django. setelah semuanya terinstal, kita memerlukan repository git khusus untuk proyek ini. setelah melakukan inisiasi git dengan local, kita dapat menjalankan perintah "django-admin startproject handuleru ."untuk membuat directory project Django didalam directory yang telah kita buat. directory tersebut akan memiliki settings.py untuk pengaturan, kita dapat menambahkan localhost dan 127.0.0.1 kedalam allowed_host agar kita dapat mengakses project kita dari localhost8000. kita dapat Melakukann push directory local kita ke git untuk tahap lebih lanjut.

Membuat aplikasi dengan nama main pada proyek tersebut.
untuk membuat aplikasi dengan nama main, kita dapat menjalankan perintah (python manage.py startapp main) didalam environment proyek kita. folder main akan tercipta secara otomatis didalam directory local kita. 

Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
agar aplikasi main dapat dijalankan dalam proyek, kita perlu menambahkan 'main' pada installed_apps di settings.py project directory.

Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib.
kita dapat membuat folder baru Bernama template pada directory main. dalam folder template, kita dapat membuat sebuah file html Bernama main.html untuk tampilan dari web kita. untuk punya saya, saya membuat variable name, price, description, location, dan duration untuk setiap produk jasa yang saya miliki. saya membangun main.html saya sebaik mungkin lalu menempatkan template_variable pada space tertentu agar bisa mengakses data dari views.py.

Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
pada views.py kita dapat mengimport render terlebih dahulu agar kita bisa menjalankan main.html dari proyek. kita dapat membuat context lalu mengisikan variable template beserta isinya didalamnya. variable template harus memiliki nama yang sama dengan variable template di main.html agar main.html dapat menampilkan nilainya. jika Namanya tidak sama, maka website nantinya tidak akan menampilkan apa apa pada section variable template.

Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
kita perlu membuat urls pada directory proyek dan main agar proyek proyek dapat terhubung dengan app main memalui url tersebut.

Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
setelah mengerjakan directory local, kita harus melakukan push directory local ke repository lalu melakukan push ke pws dengan cara menjalankan perintah git branch -M main lalu git push pws main:master. setelah itu, pada web pws, project kita akan menampilkan project build, dan apabila sudah success, kita dapat melihat perubahannya di tautan website kita.

Membuat readme.md
kita dapat membuat readme.md di directory local kita lalu melakukan push ke git. readme.md berisikan text yang ini.

===================================================================
Jelaskan fungsi git dalam pengembangan perangkat lunak!
Dalam sebuah proyek pengembangan perangkat lunak, kita membutuhkan berbagai keahlian mulai dari membuat design, fungsional, hingga membuat codingannya. Selain itu, setiap bagian dari software tersebut cukup sulit untuk dibuat sehingga kita membutuhkan sebuah tim untuk mengerjakannya. GIt merupakan sebuah Version Control System yang memungkinkan kita mengerjakan sebuah proyek dalam sebuah repository secara bersamaan. Git menyediakan sebuah directory yang dapat diakses oleh sebuah tim dengan berbagai fitur pull, push, clone, dan sebagainya. fitur fitur yang disediakan oleh git sangat berguna untuk proyek pengembangan secara tim. selain itu, kita juga dapat melacak perubahan dan versi setiap project menggunakan git. Git juga memiliki integrasi yang baik dengan banyak software pihak ketiga. oleh karena itu, git sangat berguna dalam pengembangan perangkat lunak secara tim.

===================================================================
Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Untuk awal pembelajaran, kita menggunakan framework Django karena framework tersebut cukup mudah untuk dipahami untuk pemula. Selain itu, Django project memiliki fitur ORM sehingga kita dapat mengerjakan sebuah project tanpa harus menguasai banyak Bahasa pemrograman. Framework Django juga memiliki struktur dan integrasi yang bagus dan mudah untuk dipahami. Oleh karena itu, Django merupakan framework yang bagus untuk pemula dalam software developing.

===================================================================
pada sebuah project Django terdapat file python Bernama models.py
ORM ataua Object Relational Mapping adalah sebuah protocol dimana kita bisa menghubungi atau mengakses data base yang menggunakan Bahasa SQL dengan menggunakan Bahasa lain. Models merupakan bagian dari project Django untuk mengatur database dari project. Models pada Django menggunakan python yang mengimport library Django. karena pada Django kita menggunakan Models.py untuk mengakses database, maka hal tersebut sudah termasuk dalam ORM. Bahasa python yang digunakan pada models dapat diartikan sebagai SQL statements pada database. dengan begitu kita relasi antar code dapat dimaksimalkan.