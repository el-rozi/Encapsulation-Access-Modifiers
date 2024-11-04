class Segitiga:

    def __init__(self, alas, tinggi) -> None:
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi
    
segitiga_besar = Segitiga(100, 80)

#akses variable alas, tinggi, dan luas dari luar kelas
print(f'alas : {segitiga_besar.alas}')
print(f'alas : {segitiga_besar.tinggi}')
print(f'alas : {segitiga_besar.luas}')
