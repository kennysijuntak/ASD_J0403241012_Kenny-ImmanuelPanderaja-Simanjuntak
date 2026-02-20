#========================================================
#Nama       : Kenny Immanuel P.S
#NIM        : J0403241012
#Kelas      : TPL A/1
#========================================================

#========================================================
#Implementasi Dasar : Queue
#========================================================

class Node :
    #konstruktor yang dijalankan secara otomatis ketika class node dipanggil/disintatiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next =None #pointer ini menunjuk ke nedo berikutnya (awal=none)

class queue:
    #buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #node paling depan
        self.rear = None #node paling belakang

    def is_empty(self):
        return self.front is None

    #membuat fungsi untuk menambahkan data baru pada bagian paling belakang
    def enqueue(self,data):
        nodeBaru = Node(data)

        #jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        self.rear.next = nodeBaru #letakan data baru pada setelahnya rear
        self.rear = nodeBaru # Jadikan data baru sebagai rear

    def dequeue(self):
        #jika setelah geser front menjadi none, maka queue kosong
        #rear juga harus none
        if self.front is None:
            self.rear = None
            return
        #menghapus data dari depan/front
        data_terhapus = self.front.data #lihat data paling depan
        self.front = self.front.next #geser front ke node berikutnya
        return data_terhapus

    def tampilkan(self):
        current = self.front
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("rear")
        

#instansiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
