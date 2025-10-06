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
https://drive.google.com/file/d/1NtpBEqFnlqdaq7XoJNha234NOnerAvcy/view?usp=drivesdk

Bagan tersebut menjelaskan alur kerja Django dalam menangani sebuah request dari user hingga menghasilkan response berupa halaman web. Ketika seorang user melakukan permintaan melalui browser, misalnya dengan membuka sebuah URL, permintaan tersebut pertama kali diterima dan dicocokkan oleh urls.py. File ini berperan sebagai router yang menentukan view mana yang harus dijalankan berdasarkan pola URL yang diminta. Setelah itu, permintaan diteruskan ke fungsi atau class view yang ada di views.py. View inilah yang berperan sebagai pengatur logika utama aplikasi. Jika view membutuhkan data dari database, maka ia akan memanggil model yang telah didefinisikan di models.py. Model merepresentasikan tabel pada database, sehingga setiap query data akan dilakukan melalui model, misalnya mengambil semua produk dari tabel Product. Setelah model selesai melakukan transaksi data dengan database, hasilnya dikembalikan lagi ke view.

Data yang sudah diperoleh dari model kemudian dipersiapkan dalam sebuah context dan diteruskan ke berkas template HTML. Template ini berfungsi untuk menyusun tampilan halaman web yang akan dilihat user, dengan cara menyisipkan data ke dalam struktur HTML menggunakan sintaks Django seperti {{ }}. Setelah proses rendering selesai, view mengembalikan template yang sudah berisi data tersebut sebagai response ke browser. Akhirnya, user dapat melihat halaman web dengan tampilan yang sudah rapi sekaligus menampilkan data yang diambil dari database.

Dengan demikian, urls.py, views.py, models.py, dan template HTML saling terkait dalam satu alur kerja: urls.py mengarahkan permintaan, views.py mengelola logika dan menghubungkan komponen lain, models.py menangani akses data, sedangkan template HTML menyajikan data tersebut dalam bentuk halaman web yang dapat diakses oleh user.



3. Dalam proyek Django, settings.py memiliki peran yang sangat penting karena berfungsi sebagai pusat konfigurasi. Semua pengaturan inti proyek, mulai dari keamanan melalui SECRET_KEY, pilihan mode debug untuk membedakan lingkungan lokal dan produksi, konfigurasi database yang digunakan, hingga daftar aplikasi yang terpasang, semuanya berada di dalam berkas ini. Selain itu, settings.py juga mengatur zona waktu, bahasa, static files, serta berbagai pengaturan tambahan yang memastikan proyek dapat berjalan sesuai kebutuhan.


4. Proses migrasi database di Django bekerja dengan cara mendeteksi perubahan yang terjadi pada model. Ketika kita membuat atau memodifikasi model, perintah makemigrations digunakan untuk menghasilkan file migrasi yang berisi instruksi perubahan struktur database. Selanjutnya, perintah migrate menjalankan instruksi tersebut dan memperbarui database agar sesuai dengan definisi model yang baru. Dengan kata lain, migrasi berfungsi sebagai jembatan antara kode Python yang kita tulis di models.py dan struktur nyata dari database yang digunakan.


5.Django sendiri dijadikan framework pertama untuk dipelajari karena memiliki pendekatan yang lengkap dan terstruktur. Framework ini sudah menyediakan banyak fitur bawaan, mulai dari autentikasi, ORM, hingga sistem templating, sehingga memudahkan pemula untuk langsung fokus pada konsep inti tanpa harus membangun semuanya dari nol. Django juga menggunakan pola MTV (Model–Template–View) yang membantu mahasiswa memahami arsitektur aplikasi web dengan lebih baik. Ditambah lagi, dokumentasi Django sangat lengkap, komunitasnya besar, dan framework ini mendorong penerapan best practice dalam pengembangan perangkat lunak.


6. Menurut saya pribadi, asisten dosen pada tutorial pertama sudah memberikan penjelasan yang cukup membantu dalam memahami dasar penggunaan Django. Penjelasannya jelas dan runtut, namun akan lebih baik lagi jika ditambahkan contoh-contoh error yang sering muncul ketika setup atau deployment. Dengan begitu, mahasiswa bisa lebih siap menghadapi masalah teknis yang biasanya cukup sering terjadi di tahap awal pengembangan.


Sekian dan terima kasih
Salam,
Tirta Rendy Siahaan 2406355621

Selanjutnya pada README Tugas 3 , saya izin saya izin memamparkan jawaban dari beberapa pertanyaan berikut.
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

PAPARAN 

1. Dalam pengimplementasian sebuah platform, data delivery dibutuhkan agar setiap komponen aplikasi dapat saling berkomunikasi dengan baik. Data delivery memungkinkan data dikirimkan dari satu bagian ke bagian lain secara konsisten, aman, dan dapat diskalakan. Misalnya, frontend memerlukan data dari backend dalam format tertentu agar dapat ditampilkan ke pengguna. Tanpa adanya mekanisme data delivery, pertukaran data akan menjadi sulit diatur, rentan kesalahan, dan tidak fleksibel saat platform berkembang.

2. Jika dibandingkan antara XML dan JSON, keduanya sama-sama digunakan sebagai format pertukaran data, namun JSON lebih populer dalam pengembangan modern. Hal ini karena JSON memiliki struktur yang lebih sederhana, lebih ringkas, dan mudah dipahami baik oleh manusia maupun mesin. JSON juga didukung secara native oleh JavaScript sehingga memudahkan integrasi pada aplikasi web. Sebaliknya, XML cenderung lebih verbose dengan banyak tag pembuka dan penutup. Walaupun XML memiliki keunggulan seperti dukungan schema dan transformasi data yang kuat, JSON tetap lebih dipilih karena efisiensi dan kemudahan penggunaannya dalam API dan aplikasi modern.

3. Dalam framework Django, method is_valid() pada sebuah form digunakan untuk memeriksa apakah data yang dikirim oleh pengguna sudah sesuai dengan aturan validasi yang ditentukan. Method ini sangat penting karena secara otomatis menjalankan validasi pada setiap field form, mengumpulkan error jika ada, dan menghasilkan data yang sudah dibersihkan dalam cleaned_data apabila input dinyatakan valid. Dengan demikian, is_valid() memastikan bahwa hanya data yang benar dan sesuai aturan yang akan diproses atau disimpan ke dalam basis data, sehingga mencegah terjadinya kesalahan maupun potensi masalah keamanan.

4. Penggunaan csrf_token pada form Django juga merupakan hal yang krusial. Token ini melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF), yaitu serangan yang memanfaatkan kepercayaan sebuah situs terhadap browser pengguna. Tanpa adanya csrf_token, seorang penyerang dapat membuat sebuah halaman berbahaya yang secara diam-diam mengirimkan permintaan POST ke aplikasi yang sedang login di browser korban, misalnya untuk mengubah data atau melakukan transaksi tanpa sepengetahuan pengguna. Oleh karena itu, menambahkan csrf_token memastikan bahwa setiap permintaan berasal dari form yang sah dan bukan dari sumber luar yang berbahaya.

5. Dalam mengimplementasikan checklist tugas, langkah pertama adalah membuat views baru untuk menampilkan data model dalam format XML dan JSON, baik untuk semua objek maupun berdasarkan ID. Setelah itu, dibuat routing URL agar masing-masing view dapat diakses melalui path tertentu. Selanjutnya, dibuat halaman utama yang menampilkan daftar objek dengan tombol “Add” untuk menuju halaman form penambahan data, serta tombol “Detail” yang menampilkan informasi detail tiap objek. Halaman form disiapkan menggunakan ModelForm untuk mempermudah validasi input dan penyimpanan data. Setelah itu, dibuat halaman detail untuk menampilkan informasi lengkap dari objek yang dipilih. Terakhir, seluruh pertanyaan yang diberikan dijawab pada README.md dalam bentuk paragraf untuk mendokumentasikan pemahaman terhadap konsep yang digunakan.

6. Sebagai tambahan refleksi, tutorial yang sudah diberikan asisten dosen sudah cukup membantu untuk memahami implementasi form, validasi, serta pengaturan routing pada Django. Namun, akan lebih baik jika setiap penjelasan tidak hanya fokus pada langkah teknis, tetapi juga pada alasan mengapa langkah tersebut penting dilakukan. Penambahan contoh kasus nyata serta tips debugging juga akan sangat membantu mahasiswa dalam memahami konsep yang lebih dalam, tidak sekadar mengikuti instruksi.


Berikut adalah tautan menuju laporan postman 4 URL :
https://drive.google.com/drive/folders/1sOLSVDDaiZxvOC7HXDEBRbks8Z4ZmSEo?usp=sharing

Sekian dan terima kasih
Salam,
Tirta Rendy Siahaan 2406355621


README Lanjutan untuk Tugas 4 :
1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

PAPARAN 
1. Django AuthenticationForm adalah form bawaan Django yang digunakan untuk proses autentikasi login pengguna dengan memvalidasi username dan password terhadap database user yang tersimpan. Kelebihan utama dari AuthenticationForm adalah sifatnya yang praktis karena sudah terintegrasi langsung dengan sistem autentikasi Django, sehingga developer tidak perlu membuat form login dari nol dan validasi keamanan dasar seperti password hashing sudah otomatis dijalankan. Selain itu, form ini juga mudah diperluas atau dikustomisasi sesuai kebutuhan. Namun, kekurangannya adalah sifatnya yang generik sehingga jika aplikasi memerlukan autentikasi dengan field tambahan di luar username dan password, maka developer perlu melakukan override terhadap form tersebut.

2. Autentikasi adalah proses untuk memastikan identitas pengguna, yaitu memverifikasi apakah username dan password yang dimasukkan benar, sedangkan otorisasi adalah proses pengecekan apakah pengguna yang sudah terautentikasi memiliki hak akses untuk melakukan suatu aksi atau mengakses resource tertentu. Django mengimplementasikan autentikasi melalui sistem bawaan django.contrib.auth yang menangani login, logout, dan password hashing. Untuk otorisasi, Django menyediakan mekanisme permissions dan groups yang bisa diterapkan ke model maupun view, sehingga developer dapat mengatur siapa saja yang bisa melihat, mengedit, atau menghapus suatu resource dengan decorator atau middleware.

3. Session dan cookies digunakan untuk menyimpan state pada aplikasi web, tetapi masing-masing memiliki kelebihan dan kekurangan. Cookies disimpan di sisi client sehingga sederhana dan cepat digunakan untuk melacak data kecil seperti preferensi pengguna atau token login, namun lebih rentan terhadap pencurian data (misalnya melalui serangan XSS). Session, di sisi lain, disimpan di sisi server dengan hanya ID session yang dikirim ke client melalui cookies, sehingga lebih aman karena data sensitif tidak tersimpan langsung di browser. Kekurangannya adalah session membutuhkan penyimpanan tambahan di server (misalnya database atau memori), yang bisa menambah overhead terutama pada aplikasi berskala besar.

4. Penggunaan cookies secara default tidak sepenuhnya aman karena rentan terhadap risiko seperti pencurian cookies (session hijacking) atau manipulasi data jika tidak dienkripsi dengan baik. Django menangani hal ini dengan menyediakan beberapa fitur keamanan seperti HttpOnly untuk mencegah akses cookies oleh JavaScript, Secure flag untuk memastikan cookies hanya dikirim melalui HTTPS, dan SESSION_COOKIE_AGE untuk membatasi waktu hidup session. Selain itu, Django secara default menandatangani cookies untuk mencegah pemalsuan data, sehingga meningkatkan keamanan aplikasi dalam mengelola informasi pengguna.

5. Saya mengimplementasikan checklist dengan memulai dari menambahkan sistem autentikasi menggunakan view registrasi, login, dan logout yang memanfaatkan form bawaan Django sekaligus melakukan sedikit kustomisasi sesuai kebutuhan aplikasi. Setelah itu, saya membuat dua akun pengguna secara lokal melalui admin panel maupun perintah createsuperuser lalu menambahkan masing-masing tiga dummy data pada model Product untuk setiap akun agar bisa dilakukan pengujian. Selanjutnya, saya menghubungkan model Product dengan User melalui relasi ForeignKey sehingga setiap produk memiliki pemilik yang jelas. Pada halaman utama aplikasi, saya menambahkan detail informasi pengguna yang sedang login, termasuk username serta informasi last_login yang saya simpan menggunakan cookies untuk memperlihatkan status login terakhir. Setelah semua fitur berjalan sesuai rencana, saya mendokumentasikan seluruh proses ini ke dalam README.md dan kemudian melakukan git add, git commit, dan git push ke repository GitHub agar pekerjaan dapat tersimpan dan dilacak dengan baik.


Bukti buat 2 akun dan 3 product per akun:
https://drive.google.com/file/d/1SRPqONxus0RJjUQoqtFX2MFkhcCpekav/view?usp=sharing

Salam Hormat,
Tirta Rendy Siahaan
2406355621




README untuk TUGAS 5
DAFTAR PERTANYAAN :

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!


JAWABAN :
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, browser akan menentukan prioritasnya berdasarkan aturan specificity dan urutan munculnya kode. Selector dengan tingkat specificity lebih tinggi akan diprioritaskan. Urutan tingkatannya adalah: inline style memiliki prioritas paling tinggi, kemudian selector ID, disusul oleh selector class, pseudo-class, dan attribute, lalu terakhir adalah selector elemen dan pseudo-elemen. Jika dua selector memiliki tingkat specificity yang sama, maka CSS yang ditulis paling akhir dalam file atau urutan load akan digunakan. Selain itu, deklarasi dengan !important dapat menimpa aturan lain meskipun specificity-nya lebih rendah, tetapi penggunaannya sebaiknya dihindari karena dapat menyulitkan pengelolaan kode CSS.

2. Responsive design adalah konsep penting karena aplikasi web digunakan pada berbagai perangkat dengan ukuran layar yang berbeda, mulai dari smartphone, tablet, hingga desktop. Tanpa responsive design, tampilan web bisa rusak, teks sulit dibaca, atau tombol terlalu kecil untuk diakses di layar kecil. Sebagai contoh, Instagram adalah aplikasi yang sudah menerapkan responsive design dengan baik, sehingga tampilan feed dan tombol tetap nyaman digunakan baik di smartphone maupun komputer. Sebaliknya, beberapa website lama, misalnya situs berita dengan desain tahun 2000-an, belum menerapkan responsive design sehingga tampilan kontennya melebar melebihi layar ponsel dan pengguna harus melakukan zoom in/out untuk membaca.

3. Margin, border, dan padding adalah tiga komponen penting dalam box model CSS. Margin adalah ruang di luar elemen yang memberi jarak antara elemen satu dengan lainnya. Border adalah garis yang mengelilingi elemen di antara margin dan padding, yang bisa memiliki warna, ketebalan, dan gaya tertentu. Padding adalah ruang di dalam elemen, yaitu jarak antara konten dan border elemen. Contohnya: margin: 10px; border: 2px solid black; padding: 5px; akan memberikan jarak 10 piksel di luar elemen, garis tepi hitam setebal 2 piksel, dan ruang kosong 5 piksel di dalam antara konten dengan border.

4. Flexbox dan Grid Layout adalah dua teknik layout modern di CSS. Flexbox digunakan untuk menyusun elemen dalam satu dimensi, baik secara horizontal (row) maupun vertikal (column). Flexbox sangat berguna untuk membuat tata letak navigasi, tombol yang sejajar, atau card yang rata. Grid Layout digunakan untuk menyusun elemen dalam dua dimensi (baris dan kolom) secara terstruktur. Dengan grid, kita bisa mendefinisikan area layout yang kompleks seperti halaman dashboard dengan sidebar, header, dan konten utama. Keduanya sangat membantu menghindari penggunaan float atau positioning manual yang merepotkan.

5. Implementasi checklist di atas saya lakukan secara bertahap dan mandiri, bukan sekadar mengikuti tutorial. Pertama, saya memahami dasar CSS specificity dan mencoba langsung di kode dengan membuat elemen yang memiliki class, id, dan inline style untuk melihat prioritasnya. Kedua, saya membuat halaman sederhana lalu menguji bagaimana tampilannya di berbagai perangkat dan menggunakan media query untuk membuatnya responsif. Ketiga, saya mempraktikkan box model dengan menambahkan margin, border, dan padding pada div sederhana untuk memahami perbedaannya secara visual. Keempat, saya membuat contoh layout dengan flexbox untuk navbar dan dengan grid layout untuk halaman produk. Terakhir, semua hasil percobaan saya gabungkan ke dalam proyek Django yang saya kerjakan, sehingga setiap konsep terimplementasi nyata sesuai kebutuhan aplikasi.


Salam Hormat, 
Tirta Rendy Siahaan
2406355621


INI README UNTUK TUGAS 6

PERTANYAAN DAN JAWABAN :

1. Apa perbedaan antara synchronous request dan asynchronous request?
Jawaban:
Synchronous request adalah jenis permintaan di mana browser menunggu server merespons sebelum melakukan aksi lain. Selama request berlangsung, pengguna tidak bisa berinteraksi dengan halaman, seperti halnya pada form submit tradisional. Sedangkan asynchronous request memungkinkan browser tetap berinteraksi dengan halaman meskipun permintaan sedang diproses di background. Contohnya adalah AJAX, di mana data dikirim dan diterima tanpa memerlukan reload halaman penuh.

2. Bagaimana AJAX bekerja di Django (alur request–response)?
Jawaban:
AJAX bekerja dengan mengirim request dari frontend melalui JavaScript, misalnya menggunakan fetch() atau jQuery $.ajax(), saat pengguna melakukan aksi seperti klik tombol atau submit form. Request ini dikirim ke URL endpoint yang ditangani oleh Django. Di sisi server, view Django menerima request, memproses data, dan mengembalikan response dalam format JSON atau HTML fragment. Response ini kemudian diterima oleh JavaScript di frontend, yang selanjutnya memperbarui DOM sesuai data yang diterima tanpa memuat ulang seluruh halaman.

3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
Jawaban:
Penggunaan AJAX memberikan beberapa keuntungan dibandingkan render tradisional di Django. Pertama, halaman tidak perlu reload penuh, sehingga proses lebih cepat dan efisien. Kedua, hanya bagian tertentu dari halaman yang diperbarui, sehingga menghemat bandwidth. Ketiga, AJAX membuat interaksi lebih interaktif dan real-time, misalnya validasi form dan tampilan error secara langsung tanpa berpindah halaman. Hal ini secara keseluruhan meningkatkan performa dan kenyamanan pengguna.

4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Jawaban:
Untuk menjaga keamanan saat menggunakan AJAX pada fitur Login dan Register, perlu diperhatikan beberapa hal. Pertama, selalu gunakan CSRF token pada setiap request POST untuk mencegah serangan CSRF. Kedua, jangan menaruh password di URL; gunakan metode POST dengan HTTPS untuk keamanan data. Ketiga, lakukan validasi input di sisi server, jangan hanya mengandalkan validasi di client side. Keempat, batasi percobaan login agar tidak mudah terkena brute-force attack. Terakhir, pastikan response error tidak mengandung informasi sensitif yang bisa dimanfaatkan penyerang.

5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
Jawaban:
AJAX meningkatkan pengalaman pengguna dengan mengurangi waktu tunggu karena halaman tidak perlu reload penuh. Hal ini memungkinkan pengguna melihat feedback instan, seperti loading spinner atau validasi form secara realtime. Interaksi menjadi lebih dinamis dan modern, dan pengguna bisa menerima update data secara langsung, misalnya fitur live search atau notifikasi baru. Dengan demikian, penggunaan AJAX membuat website terasa lebih responsif dan interaktif.


Salam Hormat,
Tirta Rendy Siahaan
2406355621
