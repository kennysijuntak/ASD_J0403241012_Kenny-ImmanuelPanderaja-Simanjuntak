#========================================================
#Nama       : Kenny Immanuel P.S
#NIM        : J0403241012
#Kelas      : TPL A/1
#========================================================

# ========================================================== 
# Latihan 3: Mencari Nilai Maksimum 
# ========================================================== 
 
def cari_maks(data, index=0): 
    # Base case :
    if index == len(data) - 1: # berhenti ketika index mencapai panjang list
        return data[index] 
 
    # Recursive case 
    maks_sisa = cari_maks(data, index + 1) 
    
    # akan mengembalikan nilai data dari indeks ketika data lebih besar dari nilai indeks sebelumnya
    if data[index] > maks_sisa: 
        return data[index] 
    # akan mengembalikan nilai data dari indeks sebelumnya yang lebih beasr dari nilai data indeks
    else: 
        return maks_sisa 
 
angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum:", cari_maks(angka)) 