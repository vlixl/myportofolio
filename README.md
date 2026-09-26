Nama: Leow Vincent Vintizel

NPM: 2506611856

Kelas: PBP F


# AI DISCLOSURE

Dalam pengerjaan proyek ini, saya menggunakan *ChatGPT* sesuai ketentuan berikut:
- Sarana yang digunakan hanya fitur chat, tanpa menggunakan pemrograman agentic
- **TIDAK ADA KODE DALAM PROYEK INI YANG DIMASUKKAN VERBATIM DARI AI**

Dalam pengerjaan, strategi prompting saya adalah sebagai berikut:
- Mewujudkan suasana santai dan nyaman untuk menjadikan ChatGPT sebagai teman belajar dan diskusi
- Daripada meng-copy-paste kode dari proyek ke chatgpt dan sebaliknya, saya sering menanyakan cara menyelesaikan permasalahan tersebut secara umum sebelum mengimplementasikan solusi tersebut dalam proyek
Dalam penggunaan AI, ChatGPT telah membantu terutama dalam:
- Menemukan fitur-fitur langka dari CSS yang dapat digunakan untuk menyelesaikan permasalahan tertentu
- Mengidentifikasi kompatibilitas kode dengan browser-browser yang sulit untuk diakses
- Memahami berbagai konsep-konsep baru. Dalam kasus saya, ChatGPT membantu menjelaskan konsep grid, flexbox, interactive web design, animasi, dan keyframes
Namun, terdapat pula berbagai keterbatasan dalam AI yang saya temukan:
- Salah satu permasalahan paling fundamental dari AI adalah context window. Seringkali solusi yang diberikan oleh AI masuk akal secara lokal, namun akan rusak ketika diintegrasi dengan kode proyek.
- AI sering menghasilkan sebuah positive feedback loop. Misalnya ketika saya menemukan sebuah permasalahan dan mengajukan sebuah solusi, saya akan berdiskusi dalam jangka waktu yang lama tentang bagaimana mengimplementasi solusi tersebut, meskipun terdapat solusi lain yang lebih efektif untuk digunakan.
- AI juga sering melupakan beberapa informasi yang penting, terutama dalam proyek besar yang mana permanensi memori dibutuhkan supaya tidak perlu mengulangi konteks dalam setiap percakapan.

# Refleksi Tugas

## Tugas 1

### Pertanyaan Refleksi

1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside>? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?

2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?

3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?

### Jawaban Pertanyaan Refleksi

1. Iya. HTML memberikan kerangka semantik yang dibutuhkan demi maintainability dari kode tersebut.
- Tentunya, elemen-elemen tersebut dapat diganti dengan serangkaian div, namun hal tersebut akan mengorbankan keterbacaan kode.
- Elemen-elemen semantik memberikan konteks mengenai fungsi dari masing-masing bagian halaman, sehingga struktur dokumen lebih mudah dipahami ketika kode dibaca kembali atau dikembangkan lebih lanjut.
- Elemen-elemen tersebut juga membantu memisahkan bagian-bagian utama dari website secara lebih jelas, misalnya antara navigasi, konten utama, dan section-section tertentu.
- Dengan struktur yang lebih terorganisir, pemberian styling menggunakan CSS juga menjadi lebih mudah karena setiap bagian memiliki peran yang lebih jelas.
- Selain itu, penggunaan elemen semantik membantu agar struktur halaman tidak terlalu bergantung pada nama class atau id semata untuk menjelaskan fungsi suatu elemen.

2. Tantangan utama yang saya temukan adalah bahwa tidak semua *layout* memiliki kemudahan yang setara untuk diperbesar dan diperkecil.
- Misalnya, sebuah column flex display mungkin dapat dipersempit dari samping untuk memadai viewport mobile. Namun, pada grid yang saya gunakan, susunan masing-masing elemen perlu diatur kembali ketika tidak lagi muat dalam dimensi tertentu.
- Hal lain yang menantang adalah dalam menentukan lebar-lebar viewport yang perlu ditandai dengan kode baru. 
- Sehingga, perlu diidentifikasi titik-titik fokus utama dalam setiap layout, supaya elemen-elemen pendukung dapat dipindahkan sesuai dengan layout yang memadai viewport.

3. Audio player. Ketika saya ingin menambahkan section mengenai musik yang saya kreasikan, saya dibatasi oleh audio control bawaan dari browser. 
- Hal ini mengorbankan integritas desain dari website. Meskipun Material Design Google terlihat baik pada konteksnya, terdapat situasi-situasi di mana audio control tersebut tidak terlihat sesuai pada tempatnya.
- Maka, fungsionalitas dinamis yang saya inginkan adalah tombol play/pause sendiri yang dirancang menggunakan svg dari masing-masing icon, dan menggunakan pemrograman dinamis untuk memainkan audio ketika tombol tersebut diaktifkan.

## Tugas 2

### Pertanyaan Refleksi

1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.
2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.
3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.

### Jawaban Pertanyaan Refleksi

1. Ketika pengguna membuka halaman portofolio, browser mengirimkan permintaan HTTP ke server Django. Django mencocokkan URL permintaan dengan pola pada urls.py proyek. View menerima permintaan dan menjalankan logika yang diperlukan, misalnya mengambil data pendidikan melalui model Education. Model mendefinisikan struktur data dan menyediakan akses ke database melalui ORM Django. View kemudian meneruskan data tersebut sebagai context ke template. Template mengatur penyajian data menggunakan HTML serta tag dan variabel template Django. Hasil render dikembalikan sebagai respons HTTP, lalu browser menampilkan halaman tersebut.

2. Data portofolio sebaiknya disimpan melalui model agar pengelolaan data terpisah dari pengaturan tampilan. Jika data ditulis langsung di template, setiap penambahan atau perubahan informasi mengharuskan kita mengedit HTML. Cara tersebut menyulitkan pemeliharaan, terutama ketika data semakin banyak atau digunakan di beberapa halaman. Dengan model, data dapat dikelola melalui Django admin atau fitur pengelolaan data tanpa mengubah template. Field structure dan aturan-aturan validasi juga dapat didefinisikan dengan mudah dan terpusat. Pemisahan ini memudahkan pengembangan fitur seperti pencarian, pengurutan, penyaringan, dll. Data yang sama juga dapat digunakan oleh beberapa view dengan tampilan yang berbeda.

3. makemigrations membuat file-file migrations berdasarkan perbedaan antara definisi model saat ini dan keadaan model yang tercatat dalam berkas migrasi sebelumnya. File-file tersebut berisi perubahan struktur database, tetapi belum menerapkannya ke database. Sementara itu, migrate menerapkan migrasi yang belum dijalankan ke database, sesuai urutan dependensinya. Contohnya, ketika saya menambahkan field description = models.TextField(blank=True, default="") pada model Education, saya menjalankan `python manage.py makemigrations` untuk membuat berkas migrasi penambahan field. Setelah itu, saya menjalankan `python manage.py migrate` untuk menambahkan kolom tersebut pada tabel yang terkait di database.

### Penggunaan AI Tugas 2

Dalam pengerjaan tugas, saya menggunakan AI untuk memahami konsep-konsep pada django. Saya juga menggunakan AI untuk mencari inspirasi-inspirasi desain. Sejauh ini, kekurangan AI sama dengan tugas 1, yakni kurang dapat memahami konteks proyek.

## Tugas 3

1. Kita menggunakan ModelForm dengan alasan-alasan berikut:
 a. mengurangi repetisi kode ketika mengambil data POST secara manual satu per satu dan ketika menambahkan masing-masing input dalam html
 b. menyesuaikan tipe data dengan metode input secara otomatis (misalnya input pilihan akan diberikan dropdown, input text field diberikan wadah input yang lebih besar daripada charfield)
 c. mempermudah validasi input dan inisialisasi obyek model
 d. mempermudah pemeliharaan website, karena bila Model diubah, form akan secara otomatis menyesuaikan struktur model tersebut
Dalam HTML, crsf token wajib ditambahkan sebagai bukti bahwa sebuah request benar-benar berasal dari halaman/form milik website kita, bukan dari website lain yang menipu browser user.
2. JSON lebih sering digunakan karena sintaksnya lebih jelas dan ringkas, mudah dibaca manusia, lebih ringkas, dan mudah digunakan dalam javascript (memiliki parsing sederhana).
3. Ketika fungsi view tersebut dipanggil, secara umum, obyek yang sesuai dengan model yang dipilih akan diambil dari database, kemudian difilter berdasarkan query yang diberikan dalam request. Kemudian, dengan django serializer, objek tersebut akan di-serialize menjadi bentuk JSON sebelum mengembalikannya dalam sebuah HTTP response. Alasan serialization tersebut diperlukan yakni karena objek-objek tersebut perlu diubah menjadi suatu format yang dapat dikirim dengan protokol HTTP. Dalam hal ini, JSON adalah format yang dipilih.

## Tugas 4
Dalam pengerjaan tugas 4, AI yang digunakan adalah ChatGPT. Dalam hal ini, ChatGPT digunakan untuk membantu mempercepat mengenakan style dengan gaya dan struktur yang sama untuk login, register, dan komponen-komponen lain. AI juga digunakan untuk memahami konsep-konsep mengenai authorization. 

Pada dasarnya, AI adalah mesin penerus pola. Maka, strategi prompting yang terbaik adalah dengan memberikan contoh yang baik untuk diikuti. Karena website saya memiliki desain visual yang konsisten, ChatGPT mampu membantu meneruskannya untuk mengurangi pemrograman yang berasa repetitif.
