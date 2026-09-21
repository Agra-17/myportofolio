### Project Portofolio

Name : Muh. Agra Putra Davyza Chaniago

NPM : 2506624833

Class : PBP B

### About Project
Projek ini dibuat sebagai website utama portofolio saya.  Website ini dibuat dengan Django. Tujuan dari pembuatan web ini adalah untuk belajar mengenai web development sekaligus bahasa yang di gunakan (HTML, CSS, dll), Git dan juga deployment. Projek ini juga dibuat untuk pembelajaran saya kedepannya, jadi sangat bebas jika ingin melakukan improvement.

## Local Setup

### 1. Clone the repository
```bash
git clone <repository-url>
cd portofolio
```

### 2. Create a virtual environment
```bash
python -m venv env
```

On Windows:
```bash
env\Scripts\activate
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


### AI Disclosure
Saya menggunakan AI pada projek ini. Beberapa bagian yang saya menggunakan AI adalah. Pembuatan UI dan juga sturkturisasi file css dan juga htmlnya (saya menggunakannya dengan bantuan github copilot). Saya juga mencarinya secara mendalam W3school agar memahami syntaxnya. Saya juga menggunakan AI untuk membantu saya untuk strukturisasi commit (seperti pembuatan branch dan juga commit disiplinnya). Saya juga menggunakan AI ketika adanya bug ketika ingin menambahkan foto yang berupa file. Selebihnya saya juga menggunakan AI untuk deepsearch sebagai kebutuhan saya untuk mendalami materinya.

AI assistance reference: https://claude.ai/share/69799269-6579-4abc-9eca-c6491097d70b 
AI Tools : github copilot chat  
Reference Deep Search : W3school, Youtube, dan petani kode  
-https://www.freecodecamp.org/news/how-django-mvt-architecture-works/ 
-https://www.w3schools.com/html/default.asp   
-https://www.w3schools.com/css/default.asp
-https://www.w3schools.com/django/  

### Progress Mingguan 
Pada satu minggu ini progress saya terhadap web ini adalah membuat form pada bagian achievement dan juga experience. Saya juga mempelajari bagaimana user bisa melakuakn input data dan bisa langsung ditampilkan di websitenya. Pada minggu ini juga saya mendalami alur dari penggunaan data delivery berbasis JSON. Untuk perubahan yang terjadi di website tentunya ada luamyan banyak. Adanya fitur tambah experience dan juga achievement, ada fitur untuk menghapus experience dan achievement, ada juga bagian untuk mencari achievement dan experience berdasarkan nama judulnya. Beberapa tambahan UI juga dilakukan seperti notifikasi ketika melakukan delete experience atau achievement dan juga UI mengenai pengisian form (ketika menekan tombol tambah experience atau achievement).

