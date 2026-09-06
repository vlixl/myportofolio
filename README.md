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



# Update Mingguan

Ini adalah catatan personal yang digunakan hanya untuk keperluan pribadi.

## Minggu 1

> Setiap browser memiliki kompatibilitas masing-masing, tapi Apple yang paling egois karena masih membutuhkan API WebKit.

> KODE MENAMBAHKAN GRADIEN TEKS:
>
> ```css
> background-clip: text;
> -webkit-background-clip: text;
> ```

> Git rusak terus. Harus membuat catatan cara menggunakan Git dan GitHub.
