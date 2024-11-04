# Mobil dan Mobil Balap

Proyek ini berisi implementasi kelas `Mobil` dan `MobilBalap` dalam bahasa pemrograman Python. Kelas-kelas ini digunakan untuk merepresentasikan mobil umum dan mobil balap dengan atribut dan metode yang relevan.

## Struktur Kelas

### Mobil

Kelas `Mobil` adalah kelas dasar yang memiliki atribut dan metode berikut:

- **Atribut:**
  - `__merk`: Merek mobil (private).
  - `__tahun`: Tahun pembuatan mobil (private).
  - `_kecepatan_maks`: Kecepatan maksimum mobil (protected).

- **Metode:**
  - `get_merk()`: Mengembalikan merek mobil.
  - `get_tahun()`: Mengembalikan tahun pembuatan mobil.
  - `set_kecepatan_maks(kecepatan)`: Mengatur kecepatan maksimum mobil.
  - `tampilkan_info()`: Menampilkan informasi mobil.

### MobilBalap

Kelas `MobilBalap` adalah turunan dari kelas `Mobil` dengan tambahan atribut dan metode:

- **Atribut:**
  - `__total_gear`: Total gear mobil balap (private).

- **Metode:**
  - `get_total_gear()`: Mengembalikan total gear mobil balap.
  - `tampilkan_info()`: Menampilkan informasi mobil balap, termasuk total gear.

## Contoh Penggunaan

Berikut adalah contoh cara menggunakan kelas `Mobil` dan `MobilBalap`:

```python
# Membuat objek Mobil
mobil1 = Mobil("Toyota", 2020, 180)
mobil1.tampilkan_info()

# Membuat objek MobilBalap
mobil_balap1 = MobilBalap("Ferrari", 2022, 350, 8)
mobil_balap1.tampilkan_info()


- Proyek ini di lisensikan oleh : https://github.com/el-rozi

