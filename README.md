# Praktikum Pemrograman Berorientasi Objek - Pertemuan 8

## Enkapsulasi dan Access Modifiers

Dokumen ini menjelaskan konsep enkapsulasi dalam pemrograman berorientasi objek, khususnya dalam bahasa Python, serta bagaimana menggunakan access modifiers untuk mengatur hak akses atribut dan fungsi dalam sebuah kelas.

### Pengertian Enkapsulasi

Enkapsulasi adalah konsep dalam pemrograman berorientasi objek yang digunakan untuk mengatur hak akses suatu atribut dan fungsi pada sebuah kelas. Konsep ini memungkinkan kita untuk mendefinisikan mana atribut atau fungsi yang boleh diakses secara terbuka, terbatas, atau hanya bisa diakses oleh internal kelas.

### Jenis-jenis Enkapsulasi

1. **Public Access Modifier**
   - Atribut atau variabel yang bersifat publik dapat diakses dari mana saja, baik dari dalam maupun luar kelas.

2. **Protected Access Modifier**
   - Atribut yang bersifat protected hanya dapat diakses secara terbatas oleh dirinya sendiri dan kelas turunannya. Atribut ini diawali dengan satu underscore (`_`).

3. **Private Access Modifier**
   - Atribut yang bersifat private hanya dapat diakses di dalam kelas itu sendiri. Atribut ini diawali dengan dua underscore (`__`).

### Accessor dan Mutator

Accessor (getter) dan mutator (setter) adalah fungsi yang digunakan untuk mengakses dan mengatur nilai atribut pada suatu kelas. Dalam Python, accessor didefinisikan dengan decorator `@property`, sedangkan mutator menggunakan `@<nama_atribut>.setter`.

### Contoh Penggunaan

Berikut adalah contoh penggunaan berbagai access modifiers dalam Python:

- **Public**: Semua atribut dapat diakses dari luar kelas.
- **Protected**: Atribut hanya diakses dari dalam kelas atau kelas turunannya.
- **Private**: Atribut hanya diakses dari dalam kelas itu sendiri.

### Kesimpulan

Dalam Python, access modifiers digunakan untuk mengenkapsulasi kode program, mengatur mana atribut yang boleh diakses dari luar, dan mana yang hanya diakses secara internal. Namun, perlu diperhatikan bahwa konsep "protected" dalam Python lebih merupakan konvensi daripada aturan yang ketat.


- Proyek ini di lisensikan oleh : https://github.com/el-rozi

