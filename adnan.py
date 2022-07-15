# #01 

# i = 0
# while i<4:
#     j = 0
#     while j < 4:
#         print("#", end=" ")
#         j = j+1
#     print("@")
#     i = i + 1

# # 02 ANGUSRAN

# # # 1. Jumlah Pinjaman
# # # 2. Jumlah Angsuran
# # # 3. nominal angsuran / bulan
# # # 4. jumlah kupon hadiah 

# pinjam = int(input("Masukan Nominal : "))
# bulan = int(input("Masukan Bulan  \t: "))

# #hitung angsuran / bulan
# angsuran = pinjam // bulan
# bunga = int(0.04 * pinjam)
# total = angsuran + bunga 
# print("\n\tDetail Tagihan")
# print("Total Tagihan (Bulan)\t:",total)
# x = 0
# for x in range(1, bulan + 1):
#     print("Bulan Ke-",x, "\t:",total)

# #kupon -> 1.000.000 & k0elipatan
# kupon1 = pinjam // 1000000
# print("\n\tDetail Kupon")
# print("kupon : ", kupon1)


# 03

# class Akun:
#     def presensi(self, email, password):
#         print(f"Akun dengan Email: {email} dan Password: {password} berhasil presensi")
    
# class Mahasiswa(Akun):
#     def __init__(self, nim, nama):
#         self.__nim = nim
#         self.__nama = nama
        
#     def presensi(self):
#         print(f"Mahasiswa dengan nim: {self.__nim} dengan nama: {self.__nama}")
# wanto = Akun()
# wanto.presensi("wanto@gmail.com","rahasia")
# susi = Mahasiswa(5576, "Susi")
# susi.presensi()

#04

# from zipfile import _ReadWriteMode


# from select import select
# from typing_extensions import Self


from ast import Div


class Karyawan:
    _nik = 0
    __nama = None
    __alamat = None
    __gender = None
    __divisi = None

    def __init__(self, nik= None, nama=None, email=None):
        self._nik = nik
        self.__nama = nama
        self._email = email
    #nik
    @property
    def nik(self,):
        return self._nik
    @nik.setter
    def nik(self, nik):
        self._nik = nik

    #email
    @property
    def email(self,):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email
    
    #nama
    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, nama):
        self.__nama = nama
    #alamat
    @property
    def alamat(self):
        return self.__alamat
    @alamat.setter
    def alamat(self, alamat):
        self.__alamat = alamat
    #gender
    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender):
        self.__gender = gender
    #divisi
    @property
    def divisi(self):
        return self.__divisi
    @divisi.setter
    def divisi(self, divisi):
        self.__divisi = divisi

    #hitung_gaji
    def hitung_gaji(self):
        hitung_gaji = 2000000
        print(f'Karyawan {self.__nama} Total hitung_gaji : {hitung_gaji}')
    #presensi
    def presensi(self):
        print(f'Karyawan {self.__nama} sudah presensi dengan {self._email}')

class Manager(Karyawan):
    __reward = None
    __bonus = None

    def __init__(self, reward = None, bonus =None):
        self.__reward = reward
        self.__bonus = bonus

    #reward
    @property
    def reward(self):
        return self.__reward
    @reward.setter
    def reward(self, reward):
        self.__reward = reward
        
    #bonus    
    @property
    def bonus(self):
        return self.__bonus
    @bonus.setter
    def bonus(self, bonus):
        self.__bonus = bonus

    def hitung_gaji(self):
        hitung_gaji = 5000000
        print(f'Manager {self.nama} Total hitung_gaji : {hitung_gaji} mendapat bonus = {self.bonus}')
    def presensi(self):
        print(f'Manager {self.nama} sudah presensi dengan {self.email}')

class Divisi:
    __id = None
    __nama = None
    __karyawan = []
    
    def __init__(self, id=None, nama=None):
        self.__id = id
        self.__nama = nama
    
    #id
    @property
    def id (self):
        return self.__id
    @id.setter
    def id (self, id):
        self.__id = id

    #nama
    @property
    def nama (self):
        return self.__nama
    @nama.setter
    def nama (self, nama):
        self.__nama = nama

    #karyawan
    @property
    def karyawan (self):
        return self.__karyawan

    @karyawan.setter
    def karyawan (self, karyawan):
        self.__karyawan.append(karyawan)

    def get_karyawan(self, nik):
        return self.karyawan.get(nik)

it = Divisi()
it.nama = "Divisi IT"
it.id = '01'

adnan = Karyawan()
adnan.nik = 4707
adnan.nama = "adnan"
adnan.email = "adnan@gmail.com"

ikky = Manager()
ikky.bonus = 1000000
ikky.nik = 4692
ikky.nama = "ikky"
ikky.email = "ikky@gmail.com"

it.karyawan = adnan
it.karyawan = ikky

adnan.presensi()
adnan.hitung_gaji()
print()
ikky.presensi()
ikky.hitung_gaji()


# it = Divisi('01', 'IT divisi')

# kross = Karyawan(100, 'kross','@gmail')
# ozil = Karyawan(100, 'ozil','@gmail')
# it.karyawan = kross
# it.karyawan = ozil
# kross.divisi = it
# print(kross.divisi.nama)

# ronaldo = Manager(20, 500000)
# ronaldo.nama = "ronaldo"
# ronaldo.nik = 34041222
# messi = Manager(10, 900000)
# it.karyawan = ronaldo
# it.karyawan = messi

# kross.presensi()
# kross.hitung_gaji()

# ozil.presensi()
# ozil.hitung_gaji()

print(len(it.karyawan))
for kr in it.karyawan:
    print(f' {kr.nik}-> {kr.nama}')
