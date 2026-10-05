### Project Portofolio

Name : Muh. Agra Putra Davyza Chaniago

NPM : 2506624833

Class : PBP B

### About Project
Projek ini dibuat sebagai website utama portofolio saya.  Website ini dibuat dengan Django. Tujuan dari pembuatan web ini adalah untuk belajar mengenai web development sekaligus bahasa yang di gunakan (HTML, CSS, dll), Git dan juga deployment. Projek ini juga dibuat untuk pembelajaran saya kedepannya, jadi sangat bebas jika ingin melakukan improvement.

## Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/Agra-17/myportofolio.git
cd myportofolio
```

### 2. Create a virtual environment
```bash
python -m venv env
```

On Windows (PowerShell):
```powershell
.\env\Scripts\Activate.ps1
```

On macOS/Linux:
```bash
source env/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply database migrations
```bash
python manage.py migrate
```

### 5. Run the development server
```bash
python manage.py runserver
```

Then open:
```bash
http://127.0.0.1:8000/
```

### Assignment 1
1. "Section, article dan aside" sangat membantu dalam menyusun struktur website yang baik, Hal ini sangat diperlukan karena web yang static sangat bergantung erat dengan struktur HTML. Beberapa tag tersebut mempermudah bagi pembuat website jika nantinya ada bug dan juga maintain website kedepannya. Adanya tag "section" membuat struktur pengelompokkan yang masih dalam satu kesatuan tema. Tag "article" sendiri menjadi tag yang sangat penting bagi konten atau informasi yang dapat berdiri dengan sendiri. Dan untuk tag "aside" ini merupakan tag bagi konten pendukung yang bermakna konten yang diberikan pada tag ini tidak berhubungan langsung dengan konten utamanya/sekitarnya. Dengan adanya struktur ini kode yang telah dibuat dapat dengan mudah untuk dimaintain bila ada bug dan juga lebih mudah untuk mendesainnya.  

2. Tantangan ketika membuat CSS yang responsive bagi saya adalah di pembuatan navbar. Disini saya mempelajari suatu hal yaitu overflow-x dan tidak lupa menambahkannya ke @media agar bisa untuk di atur di beberapa kondisi yang di masukkan. Untuk selebihnya karena sudah ada contoh yang diberikan dari template yaitu bentuk responsif dari fotonya, jadi bisa di ikuti untuk beberapa section seperti Education, Experience dan juga Achievement. Hal ini saya lakukan karena ketika layarnya cukup lebar (dibuka menggunakan menggunakan laptop)  bagian education dan experience saya pisahkan menggunakan grid 2 bagian, tetapi ketika diperkecil saya ubah menjadi 1 bagian kebawah saja.  

3. Batasan yang membuat saya optimal adalah belum bisa mengupdate secara real time, misalnya ketika saya memiliki experience tambahan atau achievement tambahan. Ketika hal itu terjadi saya harus menambahkannya dengan manual bukan dengan database. Hal ini juga menjadi pertimbangan saya ketika ingin membuat section project kedepannya yang mana hal itu perlu adanya database yang menyimpan project2nya saya agar tidak perlu menginput dan mendesainya secara manual. Dengan adanya iterasi yang dinamis saya dapat mengontrol project apa saja yang akan saya tampilkan dan juga ada update ketika ada project baru.  



### Assignment 2

1. Untuk alur kasarnya bisa di bentuk seperti berikut  
Dari Browser dia -> portofolio/urls.py -> main/urls.py -> main/views.py -> models.py -> template -> HTML -> Browser

Untuk secara detailnya. Pada awalnya browser meminta ke aplikasi Django, permintaan itu diterima oleh portofolio.urls (yang bertindak sebagai urls proyek). Dari url project dia akan memanggil main.urls yang terdapat di projek ini. main/urls inilah yang menentukan view mana yang akan menanggapi request ini. View disini bertugas untuk menjalankan logika aplikasi dan data yang diperlukan (mengambil data yang telah di define pada file tersebut). Untuk memperoleh datanya main/views.py akan melakukan interaksi dengan models.py yang merepresentasikan struktur data yang ada di database. Kemudian models.py bertugas untuk mengambil data yang telah ada di database kemudian di salurkan ke view.py. Setelah memperoleh data tersebut view.py akan mengirimkannya ke template. Template disini bertugas untuk mengatur display data yang telah diterima dari view tadi. Setelah selesai Django akan melakukan proses rendering (menyatukan template dan database). HTML yang telah selesai itulah yang nantinya akan dikirimkan kembali kepada browser user yang tadi memanggilnya.

2. Karena ketika kita/user ingin menambahkan/menghapus data tidak lagi perlu untuk melakukan hardcode di HTMLnya. Hal ini akan memudahkan kita/user untuk memelihara sekaligus mengembangkan website ini. Selain itu dengan menggunakan konsep template sebagai tampilan data dan model sebagai alat pengambil data, ini mempermudah kita dalam melakukan maintain terhadap website dan juga dapat memudahkan untuk melakukan pengembangan (dikarenakan kita/user tidak perlu untuk hardcode manual di template HTMLnya). Maka dari itu pemisah untuk template dan model ini sangat diperlukan untuk keberlanjutan website jangka panjang.

3. Perbedaan antara fungsi makemigrations dan migrate :  
pada makemigration Django melihat apakah ada perubahan di models.py, jika ada dia akan membuat file migrarationnya yang berisi perintah/instruksi untuk perubahan database. seperti pada contoh proyek ini adalah file 0002_achievement.py. Sedangkan migrate tugasnya untuk menjalankan perubahan yang telah dibuat oleh makemigration tadi ke database sebenarnya. Untuk simplenya makemigration adalah pembuat rancangan perintahnya dan migrate untuk mengeksekusinya ke database.

### Assignment 3  
1. Alasan mengapa menggunakan ModelForm karena dari Django sendiri sudah bisa membuat form berdasarkan model yang telah kita buat (kita memanfaatkan tools ini). Dengan adanya tools ini kita tidak perlu untuk membuat laman page html secara manual. ModelForm juga membantu dalam hal menyimpan data dan juga validasi data. Ketika perumusan di forms.py kita bisa mendefinisikan terlebih dahulu data apa yang ingin kita masukkan, sehingga nantinya dapat dengan mudah melakukan validasi data input yang diberikan user. Dengan kemudahan yang diberikan itulah ModelForm dapat membantu kita dalam maintain sebuah data inputan (berupa form) yang membuat web menjadi lebih dinamis.  

Untuk penggunaan {% csrf_token %} bersifat wajib dari Django. Selain itu, {% csrf_token %} berguna untuk keamanan sistem yang telah dibuat (terutama ketika adanya pembbuatan form). Token ini berfungsi melindungi form dari serangan CSRF (terjadi ketika pihak lain ingin mencoba mengirimkan request ke web kita menggunakan akun yang tak dikenal atau tanpa izin). Token yang dikirim akan dicek terlebih dahulu oleh Django apakah berhak untuk melakun perubahan/akses di web itu (biasanya pada method POST).  

2. Alasan utama mengapa JSON lebih disukai dari pada xml karena ukurannya yang lebih ringkas, parser yang sangat cepat, dan integrasi yang sangat natural dengan JavaScript di sisi frontend. Formating dan juga struktur yang lebih sederhana inilah yang membuat JSON lebih sering digunakan (Walaupun keduanya memiliki fungsi yang sama yaitu dapat menyimpan data). Untuk komunikasi dan juga maintain code antara frontend dan backend juga jadi lebih mudah dikarenakan struktur yang lebih sederhana dan mudah di proses juga.  

3. Secara gari besar alur yang di jalankan oleh view hingga mengembalikan data JSON adalah Browser → urls.py → view.py → model(modelform/model) → Database → Serialization(Formating data) → JSON Response → Browser.  
untuk penjelasan alurnya sebagai berikut:  
pengguna mengakses url untuk melihat data dari website portofolio dalam bentuk JSON, request ini akan dikirimkan dari browser dan diterima oleh urls.py. urls.py kemudian mengarahkan ke fungsi view yang sesuai. Selanjutnya view.py akan mengambil data dari database yang sudah di sediakan oleh model Django. Data yang diperoleh dalam proses ini masih berupa objek (QuerySet) Django, sehingga belum dapat dikirim dalam bentuk JSON. Maka dari itu, proses Serialization diperlukan, proses ini mengubah data dan objek yang "bersifat" Django menjadi format yang dapat direpresentasikan dalam bentuk JSON. Setelah itu data dikembalikan melalui JSON Response sehingga data yang bersifat JSON sudah dapat diterima kembali di web browser tersebut.  

Untuk alasan mengapa harus dilakukan serialization adalah kita tidak bisa mengirimkan data yang berupa objek Django secara langsung sebagai JSON. Maka dari itu peran dari serialization ini berfungsi sebagai jembatan bagi objek Django agar dapat dikirimkan oleh internet dengan cara melakukan formating kembali dengan format JSON(bisa dikirim dengan JSON)  

### Assignment 4
1. Debouncing adalah suatu teknik untuk menunda eksekusi sebuah program/fungsi hingga suatu jeda waktu tertentu tanpa adannya event baru yang masuk. Sebelum adanya debouncing ini perintah fetch akan langsung mengambil perintah by character yang di input dan membuat browser mengirim permintaan tersebut berkali kali (sesuai dengan berapa character yang di input). Hal ini dapat membuat workload/permintaan akan semakin banyak padahal yang ingin di input user biasanya berupa kata yang sudah memiliki makna dan tujuan, maka dari itu kita perlu wktu sejenak untuk menunggu input user yang lebih panjang dan tidak menyebabkan workload permintaan di server. Dengan adanya debouncing ini browser hanya mengirim permintaan setelah pengguna selesai mengetik dalam beberapa saat (bisa di atur untuk timernya).  

2. Ketika kita memanggil fetch sebenarnya fungsi tersebut tidak langsung mengembalikan data, dia mengembalikan Promise terlebih dahulu. Maksud dari hal ini adalah fetch memberikan perintah kepada server nanti si servernya bakal Promise(melakukan janji) untuk memberikan hasilnya nanti. Untuk await sendiri mengontrol perintah tersebut, yang mana berarti jangan lanjutkan ke baris/argumen selanjutnya sampai Promise tadi selesai/sudah ada jawabannya. Ketika sudah menerima jawaban maka hasil dari await ini lah yang akan berupa objek Response yang nantinya akan di olah menjadi json. Jika kita tidak menggunakan await kembali/return dari fetch itu merupakan Promise(belum mendapatkan hasil atau pending) yang mana Promise nantinya tidak memiliki method json untuk dapat diubah ke bentuk json (datanya tidak dapat langsung digunakan).  

3. XSS adalah serangan ketika penyerang berhasil menyisipkan kode JavaScript miliknya ke dalam halaman web yang nantinya web yang dijalankan oleh user lain akan terkena dampak dari file js tersebut. Hal ini lebih rentang terjadi di data yang di tampilkan melalui AJAX atau js karena developer seringkali memasukkan data/melakuakn input data menggunakan innerHTML dan langsung memasukkan datanya ke DOM. Selain itu, jika XSS terjadi data dari luar akan dianggap sebagai data yang boleh di eksekusi pada suatu browser. Maka dari itu developer harus secara manual memastikan data dari luar/tertentu tidak dapat dieksekusi sebagai kode pada biasanya (kita bisa handle menggunakan auto-escape atau menambahkan fungsi escape).  


### AI Disclosure
Saya memakai AI/LLM dalam pengerjaan tugas ini. Penggunaan AI yang ada dalam tugas ini beruba: Pemahaman tugas secara mendalam, mengenai alur tugas, pengaturan commit agar terstruktur, dan membantu untuk melakukan debugging saat eror terjadi. Saya juga meminta bantuan AI untuk membantu saya ketika adanya perubahan yang harus dilakukan seperti bedanya target perubahan yang dilakukan pada tutorial dan tugas ini. Tidak hanya dari AI, saya juga mendalami terlebih dahulu perihal tugas yang diberikan seperti javascript, XSS, debounce dsb. Saya menggunakan perantara youtube maupun link dokumentasi dari W3school atau dari djangonya langsung. Penggunaan AI ini saya lebih sering gunakan ketika mengalami eror pada program dan juga menanyakan pemahaman mendalam terkait materi yang akan ditugaskan pada tugas ini. Pada contohnya saya mengalami bug ketika get_achievement_jsonnya tidak muncul, saya juga mendapatkan bug ketika memunculkan notifikasi toast yang tidak sesuai, dan saya juga meminta bantuan AI untuk menyelaraskan UI yang saya miliki dengan feat yang baru saya buat. Selebihnya saya menggunakan AI ini sebagai teman diskusi ketika saya bingung dan ingin mengetahui secara mendalam bagaimana materi yang ditugaskan.

AI assistance reference: https://chatgpt.com/share/6ac34d83-8070-83ec-ab1f-596ea3117cee , https://chatgpt.com/share/6ac34d48-b9e4-83ec-ae10-d281dcdd6221 , https://chatgpt.com/share/6ac34db3-e654-83ec-bd43-1301259107bf  
AI Tools : github copilot chat, codex chat, chatGPT  
Reference Deep Search : W3school, Youtube, dan petani kode  
-https://www.freecodecamp.org/news/how-django-mvt-architecture-works/ 
-https://www.w3schools.com/html/default.asp   
-https://www.w3schools.com/css/default.asp
-https://www.w3schools.com/django/
-https://docs.djangoproject.com/en/6.1/    
-https://www.w3schools.com/js/default.asp

### Progress Mingguan 
Pada satu minggu ini progress saya terhadap web ini adalah membuat form pada bagian achievement dan juga experience. Saya juga mempelajari bagaimana user bisa melakuakn input data dan bisa langsung ditampilkan di websitenya. Pada minggu ini juga saya mendalami alur dari penggunaan data delivery berbasis JSON. Untuk perubahan yang terjadi di website tentunya ada luamyan banyak. Adanya fitur tambah experience dan juga achievement, ada fitur untuk menghapus experience dan achievement, ada juga bagian untuk mencari achievement dan experience berdasarkan nama judulnya. Beberapa tambahan UI juga dilakukan seperti notifikasi ketika melakukan delete experience atau achievement dan juga UI mengenai pengisian form (ketika menekan tombol tambah experience atau achievement).  

Pada minggu ke 4 ini progress saya terhadap web ini adalah membuat fitur login, register. Fitur ini nantinya berguna untuk plotting user (superuser,editor_user,regular_user). Saya juga menambahkan fitur baru yaitu fitur star, yang mana fitur ini berfungsi untuk pemberi tanda pada experience/achiievement tertentu yang sekiranya viewer sukai. Pada minggu ini saya juga belajar melakuakn authorization dan juga restriction di beberapa menu agar tidak semua fitur bisa akses oleh user. Dalam progress minggu ini saya juga mengubah get_experience_json saya agar transfer data yang terjadi bersifat lebih aman.

Pada minggu ke 5, progress saya terhadap web portofolio ini adalah menambahkan script(javascript) pada page page yang ada di portofolio ini. Fokus perubahan pada tugas ini ada di section achievement. Saya juga membuat toast, modal_form dan create_data menggunakan AJAX. Saya juga menambahkan/menerapkan prinsip debouncing di fitur pencariannya. Saya juga melakukan implementasi escapeHTML untuk melindungi aplikasi dari serangan XSS dan juga membersihkan input yang ada di server. Saya juga melakukan update di feat menampilkan data achievement yang sekarang di implementasi dengan AJAX. Pada minggu ini lebih fokus ke penerapan AJAX, implementasi JavaScripts dan perlindungan aplikasi terhadap XSS.

