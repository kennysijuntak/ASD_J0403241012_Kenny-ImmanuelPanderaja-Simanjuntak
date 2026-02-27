#========================================================
#Nama       : Kenny Immanuel P.S
#NIM        : J0403241012
#Kelas      : TPL A/1
#========================================================

# ========================================================== 
# Contoh Rekursi 2: Tracing Masuk/Keluar 
# ========================================================== 

def hitung(n): 
    # Base case 
    if n == 0: 
        print("Selesai") 
        return 
    
    print("Masuk:", n)      # fase stacking
    hitung(n - 1)           # pemangggilan rekursif  
    print("Keluar:", n)     # fase unwinding

hitung(3) 