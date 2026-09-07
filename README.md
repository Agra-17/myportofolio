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
cd myportofolio
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

## Project Structure
```bash
myportofolio/
├── manage.py
├── requirements.txt
├── portofolio/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── templates/
├── static/
└── db.sqlite3
```


### Assignment 1

1. <Section>, <article> dan <aside> sangat membantu dalam menyusun struktur website yang baik, Hal ini dangat diperlukan karena web yang static sangat bergantung erat dengan struktur HTML. Beberapa tag tersebut mempermudah bagi pembuat website jika nantinya ada bug dan juga maintain website kedepannya. Adanya tag <Section> membuat struktur pengelompokkan yang masih dalam satu kesatuan tema. Tag <article> sendiri menjadi tag yang sangat penting bagi konten atau informasi yang dapat berdiri dengan sendiri. Dan untuk tag <aside> ini merupakan tag bagi konten pendukung yang bermakna konten yang diberikan pada tag ini tidak berhubungan langsung dengan konten utamanya/sekitarnya. Dengan adanya struktur ini kode yang telah dibuat dapat dengan mudah untuk dimaintain bila ada bug dan juga lebih mudah untuk mendesainnya.

2. Tantangan ketika membuat CSS yang responsive bagi saya adalah di pembuatan navbar. Disini saya mempelajari suatu hal yaitu overflow-x dan tidak lupa menambahkannya ke @media agar bisa untuk di atur di beberapa kondisi yang di masukkan. Untuk selebihnya karena sudah ada contoh yang diberikan dari template yaitu bentuk responsif dari fotonya, jadi bisa di ikuti untuk beberapa section seperti Education, Experience dan juga Achievement. Hal ini saya lakukan karena ketika layarnya cukup lebar (dibuka menggunakan menggunakan laptop)  bagian education dan experience saya pisahkan menggunakan grid 2 bagian, tetapi ketika diperkecil saya ubah menjadi 1 bagian kebawah saja.

3. Batasan yang membuat saya optimal adalah belum bisa mengupdate secara real time, misalnya ketika saya memiliki experience tambahan atau achievement tambahan. Ketika hal itu terjadi saya harus menambahkannya dengan manual bukan dengan database. Hal ini juga menjadi pertimbangan saya ketika ingin membuat section project kedepannya yang mana hal itu perlu adanya database yang menyimpan project2nya saya agar tidak perlu menginput dan mendesainya secara manual. Dengan adanya iterasi yang dinamis saya dapat mengontrol project apa saja yang akan saya tampilkan dan juga ada update ketika ada project baru.

### AI Disclosure
Proyek ini menggunakan bantuan AI untuk membantu saya ketika memahami dan juga menguide ketika saya ingin melakukan perubahan ataupun ketika ada bug. Hal yang paling membantu bagi saya, yaitu membantu untuk mendesain dan membuat struktur file CSS terlihat lebih rapih. Saya menggunakan AI dengan dengan melihat terlebih dahulu referensi website portofolio kemudian menanyakan apa yang bisa saya tambahkan dan juga improve. Informasi yang diberikan pun saya kembali dalami menggunakan beberapa website seperti W3schools dan juga tutorial di Youtube.

AI assistance reference: https://claude.ai/share/a32fe957-994b-4df2-a7ef-426cc767986c  
AI Tools : github copilot chat  
Reference Deep Search : W3school, Youtube, dan petani kode  
-https://www.petanikode.com/tutorial/css/  
-https://www.w3schools.com/html/default.asp   
-https://www.w3schools.com/css/default.asp  
-https://www.youtube.com/watch?v=FZVLz5_RNho   

