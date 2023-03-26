# Nama    : Aini Salsabila
# NIM     : 210511065
# Kelas   : R2/B


print('\nSingle Inheritance_DATA\n\n')

class diri:

    def __init__(self):
        self.nama = "Aini Salsabila"
        self.umur = 21
    
    def info(self):
        print('Nama\t\t: ',self.nama)
        print(f'Umur\t\t:  {self.umur} Tahun')

class data(diri):
    def __init__(self):
        super().__init__()
        self.status = "Mahasiswa"
        self.univ = "Universitas Muhammadiyah Cirebon"
        self.prodi = "Teknik Informatika"
        self.alamat = "Brebes\n"

    def display(self):
        print('Status\t\t: ',self.status)
        print('Universitas\t: ',self.univ)
        print('Jurusan\t\t: ',self.prodi)
        print('Alamat\t\t: ',self.alamat)

a = data()
a.info()
a.display()