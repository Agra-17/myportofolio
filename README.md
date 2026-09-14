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

### AI Disclosure
Saya menggunakan bantuan AI dalam pembuatan projek ini. Penggunaan AI disini saya peruntukkan untuk memperjelas apa yang harus saya lakukan secara step by step. Untuk perihal desain saya juga meminta untuk AI saya memberikan saran agar desainnya menarik. Selain itu saya juga terkadang meminta penjelasan ketika ada hal yang misalnya saya tidak pahami, tetapi saya lebih sering mencari tahunya lewat laman pencarian (web dll) ataupun source youtube. Untuk pembuatan tests.py juga saya meminta bantuan AI agar fungsi yang telah saya bikin sebelumnya dapat berjalan sesuai dengan yang diinginkan.

AI assistance reference: https://claude.ai/share/69799269-6579-4abc-9eca-c6491097d70b 
AI Tools : github copilot chat  
Reference Deep Search : W3school, Youtube, dan petani kode  
-https://www.freecodecamp.org/news/how-django-mvt-architecture-works/ 
-https://www.w3schools.com/html/default.asp   
-https://www.w3schools.com/css/default.asp  
-https://www.youtube.com/watch?v=FZVLz5_RNho   

