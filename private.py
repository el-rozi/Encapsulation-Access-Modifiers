class Mobil:
    def __init__(self, tahun):
        self.tahun = tahun

    @property
    def tahun(self):
        return self._tahun
    @tahun.setter
    def tahun(self, tahun):
        if tahun > 2021:
            self._tahun = 2021
        elif tahun < 1990:
            self._tahun = 1990
        else:
            self._tahun = tahun

sedan = Mobil(2200)

#tidak error
#print(f'Mobil ini di buat tahun {sedan.tahun}')

#error
print(f'Mobil ini di buat tahun {sedan.tahun}')