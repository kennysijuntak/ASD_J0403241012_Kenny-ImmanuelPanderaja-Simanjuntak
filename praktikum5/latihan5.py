#========================================================
#Nama       : Kenny Immanuel P.S
#NIM        : J0403241012
#Kelas      : TPL A/1
#========================================================

# ========================================================== 
# Studi Kasus: Generator PIN 
# ========================================================== 
 
def buat_pin(panjang, hasil=""): 
    
    # Base case: jika panjang string sudah n, cetak PIN: hasil
    if len(hasil) == panjang: 
        print("PIN:", hasil) 
        return 
    
    # Choose + Explore: tambah nilai indeks angka
    for angka in ["0", "1", "2"]: 
        buat_pin(panjang, hasil + angka) 
 
buat_pin(3)