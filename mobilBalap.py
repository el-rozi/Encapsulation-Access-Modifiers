class Mobil:
    def __init__(self, merk, tahun, kecepatan_maks):
        self.__merk = merk               
        self.__tahun = tahun           
        self._kecepatan_maks = kecepatan_maks 

    def get_merk(self):                  
        return self.__merk

    def get_tahun(self):                
        return self.__tahun

    def set_kecepatan_maks(self, kecepatan): 
        self._kecepatan_maks = kecepatan

    def tampilkan_info(self):          
        print(f"Merk: {self.get_merk()}, Tahun: {self.get_tahun()}, Kecepatan Maks: {self._kecepatan_maks} km/jam")

class MobilBalap(Mobil):
    def __init__(self, merk, tahun, kecepatan_maks, total_gear):
        super().__init__(merk, tahun, kecepatan_maks)
        self.__total_gear = total_gear  

    def get_total_gear(self):          
        return self.__total_gear

    def tampilkan_info(self):          
        super().tampilkan_info()       
        print(f"Total Gear: {self.get_total_gear()}")

# Contoh penggunaan
mobil1 = Mobil("Toyota", 2020, 180)
mobil1.tampilkan_info()

mobil_balap1 = MobilBalap("Ferrari", 2022, 350, 8)
mobil_balap1.tampilkan_info()