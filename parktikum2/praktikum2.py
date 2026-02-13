#========================================================
#Praktikum  2 : Konsep ADT dan file handling (STUDI KASUS)
#Latihan    1 : Membuat fumgsi load data
#========================================================

#variabel menyimpan data
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} #inisialisai data dictionary
    with open(nama_file,"r",encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(",")
            data_dict[nim] = {"nama": nama, "nilai":int(nilai)}
    return data_dict

buka_data = baca_data(nama_file) #memanggil fungsi load data dan menyimpan dalam variable
#print("jumlah data terbaca", len(buka_data)) #melihat berapa data yang di load

#========================================================
#Praktikum  2 : Konsep ADT dan file handling (STUDI KASUS)
#Latihan    2 : membuat fungsi menamplikan data
#========================================================

def tampilkan_data(data_dict):
    #membuat header tabkle
    print("\n========= DAFTAR MAHASISWA ==========")
    print(f"| {'NIM' :<10} | {'Nama' :<12} | {'Nilai' :>5} |")
    '''
    untuk tampilan yang rapi, atur lebar kolom
    {'NIM' :<10} artinya nim rata kiri dengan lebar kolom 10 karakter
    {'Nama' :<12} artinya nim rata kiri dengan lebar kolom 10 karakter
    {'Nilai' :>5} artinya nim rata kiri dengan lebar kolom 10 karakter

    '''
    print("-"*37) #membuat garis

    #menampilkan isi datanya
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"| {nim :<10} | {nama :<12} | {int(nilai) :>5} |")
    print("-"*37) #membuat garis

#tampilkan_data(buka_data) #memanggil fungsi untuk menampilkan data

#========================================================
#Praktikum  2 : Konsep ADT dan file handling (STUDI KASUS)
#Latihan    3 : membuat fungsi mencari data
#========================================================

#membuat fungsi pencarian data
def cari_data(data_dict):
    #pencarian data berdasarkan nim sebagai key dictionary
    #membuat input nim mahasiswa yang akan dicari
    nim_cari = input("Masukan NIM mahasiswa yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("===== Data Mahasiswa Ditemukan =====")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print("Data tidak ditemukan. pastikan NIM yang dimasukan benar")

#memanggil fungsi cari data
#cari_data(buka_data)

#========================================================
#Praktikum  2 : Konsep ADT dan file handling (STUDI KASUS)
#Latihan    4 : Membuat fungsu Update Data
#========================================================

#membuat fungsi update data
def ubah_data(data_dict):
    
    #awali dulu dengan mencari nim / data mahasiswa yang ingin di update
    nim = input("Masukan NIM mahasiswa yang ingin diubah data: ").strip()
    
    if nim not in data_dict:
        print("NIM tidak ditemukan. update dibatalkan")
        return
    try:
        nilai_baru = int(input("masukan nilai baru 0-100 : ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. Update dibatalakan")
    
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#memanggil fungsi ubah data
#ubah_data(buka_data)

#========================================================
#Praktikum  2 : Konsep ADT dan file handling (STUDI KASUS)
#Latihan    5 : Membuat fungsu Menyimpan Data pada File
#========================================================

#membuat fungsi Menyimpan data ke file
def simpan_data(nama_file, data_dict):
    with open(nama_file,"w",encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")
            print("\nData Berhasil disimpan ke file")

#memanggil fungsi simpan data
#simpan_data(nama_file, buka_data)

#========================================================
#Praktikum  2 : Konsep ADT dan file handling (STUDI KASUS)
#Latihan    6 : Membuat Menu Interaktif
#========================================================

def main():
    #load data otomatis saat program dimulai
    buka_data = baca_data(nama_file)

    while True:
        print("\n=== MENU DATA MAHASISWA ===")
        print("1. Tampilkan data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan Data ke file")
        print("0. keluar")

        pilihan = input("Pilih Menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data) #memanggil fs.2 menampilkan data
        elif pilihan == "2":
            cari_data(buka_data) #memanggil fs.3 mencari data
        elif pilihan =="3":
            ubah_data(buka_data) #memanggil fs.4 mengubah data
        elif pilihan == "4":
            simpan_data(nama_file,buka_data) #memanggil fs.5 menyimpan data ke file
            print("Data Berhasil disimpan ke file")
        elif pilihan == "0":
            print("Program Selesai")
            break

        else:
            print("pilihan tidak valid")

main()