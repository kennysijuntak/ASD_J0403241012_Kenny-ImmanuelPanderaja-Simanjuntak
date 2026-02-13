class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
    
    def search(self, key): 
        if not self.head:
            print("list kosong")
            return False
        current = self.head
        while True:
            if current.data == key:
                print(f"data {key} ditemukan dalam linked list")
                return True
            current = current.next
            if current == self.head:
                break
        print("data tidak ditemukan")
        return False


    def display(self):
        if not self.head:
            print("List is empty")
            return
        print("Circular Singly Linked List:")
        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next
        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("...(back to head)")

cll = CircularSinglyLinkedList()	
cll.insert_at_end(3)	
cll.insert_at_end(5)	
cll.insert_at_end(13)	
cll.insert_at_end(2)	
cll.display()	

search = int(input("Masukan elemen yang ingin dicari : "))
cll.search(search)
