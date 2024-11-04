class Mobil:
    def __init__(self, merk):
        self._merk = merk

class MobilBalap(Mobil):
    def __init__(self, merk, total_gear):
        super().__init__(merk)
        self._total_gear = total_gear

    def pamer(self):
        #akses _merk dari subclass
        print(f"ini mobil {self._merk} dengan total gear {self._total_gear}")

#bikin objek dari kelas mobil balap
ferrari = MobilBalap("Ferrari", 8)
ferrari.pamer()  # Tambahkan tanda kurung di sini