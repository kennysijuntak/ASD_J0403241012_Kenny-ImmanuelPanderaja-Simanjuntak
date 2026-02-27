#========================================================
#Nama       : Kenny Immanuel P.S
#NIM        : J0403241012
#Kelas      : TPL A/1
#========================================================

# ========================================================== 
# Latihan 1: Rekursi Pangkat 
# ========================================================== 

def pangkat(a, n): 
    # Base case 
    if n == 0: # berhenti ketika n = 0
        return 1 

    # Recursive case: masalah diperkecil menjadi pangkat(a,n-1)
    return a * pangkat(a, n - 1) 

print(pangkat(2, 4))  # Output: 16 