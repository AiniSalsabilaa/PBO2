#contoh1
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def belajar(self):
        print(self.nama, "sedang belajar")
class Pekerja:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    def bekerja(self):
        print(self.nama, "sedang bekerja")
class MahasiswaPekerja(Mahasiswa, Pekerja):
    def __init__(self, nama, nim, pekerjaan):
        Mahasiswa.__init__(self, nama, nim)
        Pekerja.__init__(self, nama, pekerjaan)
    def bersosialisasi(self):
        print(self.nama, "sedang bersosialisasi")
mhs_pekerja = MahasiswaPekerja("Rahma", "190001", "Programmer")
mhs_pekerja.belajar() # output: Rahma sedang belajar
mhs_pekerja.bekerja() # output: Rahma sedang bekerja
mhs_pekerja.bersosialisasi() # output: Rahma sedang bersosialisasi

#contoh2
class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")
class Reptil:
    def __init__(self, jenis, habitat):
        self.jenis = jenis
        self.habitat = habitat
    def display_info(self):
        print(f"Jenis: {self.jenis}")
        print(f"Habitat: {self.habitat}")
class Amphibi:
    def __init__(self, metamorfosis, habitat):
        self.metamorfosis = metamorfosis
        self.habitat = habitat
    def display_info(self):
        print(f"Metamorfosis: {self.metamorfosis}")
        print(f"Habitat: {self.habitat}")
class Katak(Reptil, Amphibi):
    def __init__(self, nama, umur, jenis, habitat, metamorfosis):
        Hewan.__init__(self, nama, umur)
        Reptil.__init__(self, jenis, habitat)
        Amphibi.__init__(self, metamorfosis, habitat)
    def display_info(self):
        super().display_info()
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")
        print(f"Jenis: {self.jenis}")
        print(f"Habitat: {self.habitat}")
        print(f"Metamorfosis: {self.metamorfosis}")
# contoh penggunaan
katakA = Katak("Katak Hijau", 2, "Reptil-Amphibi", "Air", "Telur")
katakA.display_info()

#contoh3
class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")
class Pekerja:
    def __init__(self, pekerjaan, gaji):
        self.pekerjaan = pekerjaan
        self.gaji = gaji
    def display_info(self):
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")
class Penulis:
    def __init__(self, buku, genre):
        self.buku = buku
        self.genre = genre
    def display_info(self):
        print(f"Buku: {self.buku}")
        print(f"Genre: {self.genre}")
class PenulisPekerja(Orang, Pekerja, Penulis):
    def __init__(self, nama, umur, pekerjaan, gaji, buku, genre):
        Orang.__init__(self, nama, umur)
        Pekerja.__init__(self, pekerjaan, gaji)
        Penulis.__init__(self, buku, genre)
    def display_info(self):
        super().display_info()
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")
        print(f"Buku: {self.buku}")
        print(f"Genre: {self.genre}")
# contoh penggunaan
penulis_pekerjaC = PenulisPekerja("Jane Doe", 30, "Penulis", "$5000", "The Book", "Fiksi")
penulis_pekerjaC.display_info() 
