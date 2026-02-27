#========================================================
#Nama       : Kenny Immanuel P.S
#NIM        : J0403241012
#Kelas      : TPL A/1
#========================================================

# ========================================================== 
# Latihan 2: Tracing Rekursi 
# ========================================================== 
 
def countdown(n): 
    # base case
    if n == 0: 
        print("Selesai") 
        return 
 
    print("Masuk:", n) 
    # fase stacking
    countdown(n - 1) 
    # pemanggilan rekursif
    print("Keluar:", n) 
    # face unwinding
 
countdown(3) 