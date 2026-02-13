#========================================================
#Praktikum1 : Konsep ADT dan File Handling
#Latihan Dasar 1 : Membaca seluruh isi file data
#========================================================

print("====Membuka file dalam satu string====")
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

#mengetahui tipe data file
print("Tipe data :",type(isi_file))

print("====Membuka file perbaris====")
jumlah_baris = 0
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
        print("baris ke-",jumlah_baris)
        print("isinya :",baris)

#========================================================
#Praktikum1 : Konsep ADT dan File Handling
#Latihan Dasar 1 : Membaca seluruh isi file data
#========================================================

with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilang karakter baris baru
        nim, nama, nilai = baris.split(",") #Pecah menjadi data satuan dan simpan ke variabel
        print("NIM :", nim, "| Nama :", nama, "| Nilai :", nilai)

#========================================================
#Praktikum1 : Konsep ADT dan File Handling
#Latihan Dasar 1 : Membaca seluruh isi file data list
#========================================================

data_list = [] #inisialisai list untuk menampung data

with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilang karakter baris baru
        nim, nama, nilai = baris.split(",")
        data_list.append([nim,nama,int(nilai)]) #Menyimpan data ke list
print("=== Menampilkan list ===")
print(data_list)
print("Contoh Record ke-1", data_list[0])
print("Contoh Record ke-2", data_list[1])


#========================================================
#Praktikum1 : Konsep ADT dan File Handling
#Latihan Dasar 1 : Membaca seluruh isi file data dictionary
#========================================================

data_dict = {} #inisialisai ditionary

with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilang karakter baris baru
        nim, nama, nilai = baris.split(",")
        #simpan data dalam dictionary
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
print ("=== Menampilka data dictionary ===")
print(data_dict)