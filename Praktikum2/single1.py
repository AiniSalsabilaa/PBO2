# Nama    : Aini Salsabila
# NIM     : 210511065
# Kelas   : R2/B


print('\nSingle Inheritance_NASI GORENG\n\n')

class Menu:
    def __init__(self,menu,level):
        self.menu = menu
        self.level = level

    def info(self):
        print('Menu\t\t: ',self.menu)
        print('Level\t\t: ',self.level)

class Pesan(Menu):
    def __init__(self,menu,level,topping,tambahan):
        super().__init__(menu,level)
        self.topping = topping
        self.tambahan = tambahan
       
    def pesan(self):
        print('Topping\t\t: ',self.topping)
        print('Tambahan\t: ',self.tambahan)

pesan1 = Pesan("Nasi Goreng",3,"Telur Dadar","Tidak pake sayuran\n")
pesan1.info()
pesan1.pesan()


pesan2 = Pesan("Baso","Pedas Banget","Kerupuk","-\n")
pesan2.info()
pesan2.pesan()