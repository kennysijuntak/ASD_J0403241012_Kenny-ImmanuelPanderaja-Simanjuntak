#========================================================
#Nama       : Kenny Immanuel P.S
#NIM        : J0403241012
#Kelas      : TPL A/1
#========================================================

# ========================================================== 
# Latihan 4: Kombinasi Huruf 
# ========================================================== 
 
def kombinasi(n, hasil=""): 
    # Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n: 
        print(hasil) 
        return 
    
    kombinasi(n, hasil + "A") # Choose + Explore: tambah 'A' 
    kombinasi(n, hasil + "B") # Choose + Explore: tambah 'B' 
 
kombinasi(2) 