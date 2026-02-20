#========================================================
#Nama       : Kenny Immanuel P.S
#NIM        : J0403241012
#Kelas      : TPL A/1
#========================================================

#========================================================
#Implementasi Dasar : Node pada Linked List
#========================================================

class Node :
    #konstruktor yang dijalankan secara otomatis ketika class node dipanggil/disintatiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next =None #pointer ini menunjuk ke nedo berikutnya (awal=none)

#1.) membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2.) menghubungkan node : A -> B -> c -> none
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3.)trafesal =  Menulusuri dari head sampai ke none
current = head
while current is not None:
    print(current.data) #menampilkan data pada node start
    current = current.next #pindah ke node berikutnya

#========================================================
#Implementasi Dasar : stack
#========================================================