#========================================================
#Nama       : Kenny Immanuel P.S
#NIM        : J0403241012
#Kelas      : TPL A/1
#========================================================

#========================================================
#Implementasi Dasar : stack
#========================================================

class Node :
    #konstruktor yang dijalankan secara otomatis ketika class node dipanggil/disintatiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next =None #pointer ini menunjuk ke nedo berikutnya (awal=none)

#stacl ada operasi push(memasukan head baru) dan pop(menghapus head)

class stack:
    def __init__(self): #memasukan data baru pada stack
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)

    def is_empty(self):
        return self.top is None #stack kosong jika top = None
    
    def push(self,data):
        #1.) membuat node baru
        nodeBaru = Node(data) #instantiasi/memanggile konstruktor pada class node

        #2.) node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top

        #3.0 geser top pindah ke node baru
        self.top = nodeBaru

    def pop(self): #mangambil/menghapus node paling atas (top/head)
        
        if self.is_empty():
            print("Stack Kosonng, tidak bisa pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dan simpen di variabel
        # B -> A -> none
        self.top = self.top.next #menggeser top ke node berikutnya
        return data_terhapus
    
    def peek(self):
        #melihat data yang paling atas tanpa menghapusnya
        if self.is_empty():
            return None
        return self.top #BLOMMMM SELESAIIIIII

    def tampilkan(self):
        #Top -> A -> B
        current = self.top
        print("top ", end="-> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#instantiasi Class stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (lihat top) :",s.peek) #LANJUTANNYA APA???? 
s.pop()
s.tampilkan()
s.pop()
s.tampilkan()
s.pop()
s.tampilkan()
s.pop()
