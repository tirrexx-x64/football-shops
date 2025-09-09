Berikut adalah tautan menuju aplikasi PWS yang sudah saya deploy:
https://tirta-rendy-footballshops.pbp.cs.ui.ac.id/

Baik, saya izin memamparkan jawaban dari beberapa pertanyaan berikut.
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan peran settings.py dalam proyek Django!
4. Bagaimana cara kerja migrasi database di Django?
5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

PAPARAN

1. Untuk membuat sebuah proyek Django baru, maka yang saya lakukan adalah sebagai berikut :

Pertama, saya memulai dengan membuat sebuah folder kerja baru dan menginisialisasi proyek Django menggunakan perintah django-admin startproject <nama_proyek>. Dari perintah ini, Django otomatis membangkitkan struktur proyek awal yang sudah siap dipakai, terdiri dari file utama manage.py serta direktori proyek yang berisi konfigurasi inti seperti settings.py, urls.py, dan beberapa file penting lainnya. Setelah proyek berhasil terbentuk, saya melanjutkan dengan membuat sebuah aplikasi bernama main menggunakan perintah python manage.py startapp main. Dari sini, Django membangkitkan struktur aplikasi standar yang terdiri dari models.py, views.py, urls.py, dan file pendukung lain yang akan digunakan untuk membangun fitur.

Supaya aplikasi main ini dikenali oleh Django, saya menambahkan nama aplikasinya ke dalam INSTALLED_APPS yang ada di file settings.py. Setelah itu, saya melakukan konfigurasi routing di urls.py milik proyek utama dengan menambahkan baris path('', include('main.urls')). Dengan konfigurasi ini, setiap request yang masuk ke server akan diarahkan ke sistem routing milik aplikasi main, sehingga aplikasi dapat berjalan sesuai alur yang diharapkan.

Langkah berikutnya adalah membuat model bernama Product di dalam models.py. Model ini dibuat dengan menurunkan models.Model dan memiliki sejumlah atribut wajib, yaitu name untuk menyimpan nama produk, price untuk harga, description untuk deskripsi produk, thumbnail untuk menyimpan URL gambar, category untuk kategori, serta is_featured yang digunakan untuk menandai apakah produk termasuk unggulan atau tidak. Tipe data yang digunakan mengikuti instruksi, misalnya CharField, IntegerField, TextField, URLField, hingga BooleanField.

Setelah itu, saya beralih ke views.py untuk membuat sebuah fungsi yang bertugas menyiapkan data berupa context. Data context ini berisi informasi nama aplikasi, nama mahasiswa, dan kelas, lalu dipassing ke file template HTML agar dapat ditampilkan dengan baik di browser. Untuk menghubungkan fungsi ini dengan URL tertentu, saya menambahkan routing baru di urls.py milik aplikasi main. Misalnya, path kosong '' diarahkan langsung ke fungsi show_main sehingga halaman utama aplikasi bisa diakses lewat alamat root.

Setelah semua berjalan lancar di lokal, saya melanjutkan ke tahap deployment menggunakan PWS (Practicum Web Service). Pada tahap ini, saya memastikan bahwa environment variable seperti DATABASE_URL, DEBUG, dan SECRET_KEY sudah diatur dengan benar. Deployment dilakukan dengan cara melakukan commit perubahan ke repository Git dan kemudian push ke branch yang sudah terhubung dengan PWS, sehingga sistem otomatis membangun ulang aplikasi dengan konfigurasi terbaru.

Terakhir, saya membuat file README.md di root proyek. File ini saya isi dengan tautan menuju aplikasi PWS yang sudah berhasil di-deploy, serta jawaban atas pertanyaan reflektif seperti bagaimana cara kerja migrasi database di Django, apa peran dari settings.py, mengapa Django dipilih sebagai framework pertama untuk dipelajari, dan juga feedback terhadap asisten dosen tutorial sebelumnya. Dengan demikian, README.md tidak hanya berfungsi sebagai dokumentasi teknis, tetapi juga sebagai sarana refleksi terhadap proses belajar yang sudah dijalani.


2. Untuk link terhadap bagan yang telah saya buat adalah sebagai berikut :
- https://drive.google.com/file/d/1NtpBEqFnlqdaq7XoJNha234NOnerAvcy/view?usp=drivesdk



3. Dalam proyek Django, settings.py memiliki peran yang sangat penting karena berfungsi sebagai pusat konfigurasi. Semua pengaturan inti proyek, mulai dari keamanan melalui SECRET_KEY, pilihan mode debug untuk membedakan lingkungan lokal dan produksi, konfigurasi database yang digunakan, hingga daftar aplikasi yang terpasang, semuanya berada di dalam berkas ini. Selain itu, settings.py juga mengatur zona waktu, bahasa, static files, serta berbagai pengaturan tambahan yang memastikan proyek dapat berjalan sesuai kebutuhan.


4. Proses migrasi database di Django bekerja dengan cara mendeteksi perubahan yang terjadi pada model. Ketika kita membuat atau memodifikasi model, perintah makemigrations digunakan untuk menghasilkan file migrasi yang berisi instruksi perubahan struktur database. Selanjutnya, perintah migrate menjalankan instruksi tersebut dan memperbarui database agar sesuai dengan definisi model yang baru. Dengan kata lain, migrasi berfungsi sebagai jembatan antara kode Python yang kita tulis di models.py dan struktur nyata dari database yang digunakan.


5.Django sendiri dijadikan framework pertama untuk dipelajari karena memiliki pendekatan yang lengkap dan terstruktur. Framework ini sudah menyediakan banyak fitur bawaan, mulai dari autentikasi, ORM, hingga sistem templating, sehingga memudahkan pemula untuk langsung fokus pada konsep inti tanpa harus membangun semuanya dari nol. Django juga menggunakan pola MTV (Model–Template–View) yang membantu mahasiswa memahami arsitektur aplikasi web dengan lebih baik. Ditambah lagi, dokumentasi Django sangat lengkap, komunitasnya besar, dan framework ini mendorong penerapan best practice dalam pengembangan perangkat lunak.


6. Menurut saya pribadi, asisten dosen pada tutorial pertama sudah memberikan penjelasan yang cukup membantu dalam memahami dasar penggunaan Django. Penjelasannya jelas dan runtut, namun akan lebih baik lagi jika ditambahkan contoh-contoh error yang sering muncul ketika setup atau deployment. Dengan begitu, mahasiswa bisa lebih siap menghadapi masalah teknis yang biasanya cukup sering terjadi di tahap awal pengembangan.


Sekian dan terima kasih
Salam,
Tirta Rendy Siahaan 2406355621
