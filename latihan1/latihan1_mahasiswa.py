class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
    def info(self):
        print(f"Nama: {self.nama}\nNIM: {self.npm} \n")
mahasiswaB = Mahasiswa("Aini Salsabila", "210511065")
mahasiswaB.info()