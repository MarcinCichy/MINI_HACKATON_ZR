class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Wstaw nowy węzeł na początku listy."""
        new_node = Node(data)
        new_node.next = self.head

        self.head = new_node

    def insert_at_end(self, data):
        """Dodaj nowy węzeł na końcu listy."""
        new_node = Node(data)
        new_node.next = None
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def insert_at_position(self, data, key):
        """Wstaw nowy węzeł za określonym key (gdzie key, to wartość."""
        new_node = Node(data)
        new_node.next = None
        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node is not None:
            if current_node.data == key:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    def delete_from_beginning(self):
        """Usuń węzeł z początku listy."""
        if not self.head:
            print("Lista jest pusta")
            return
        self.head = self.head.next

    def delete_from_end(self):
        """Usuń węzeł z końca listy."""
        if not self.head:
            print("Lista jest pusta")
            return
        if not self.head.next:
            self.delete_from_beginning()
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        current_node.next = None

    def delete_node(self, key):
        """Usuń węzeł zawierający określone dane."""
        if not self.head:
            print("Lista jest pusta")
            return
        if self.head.data == key:
            self.head = self.head.next

        current = self.head
        previous = None
        while current:
            if current.data == key:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
            else:
                previous = current
                current = current.next

    def search(self, key):
        """Znajdź węzeł zawierający dane, zwróć referencję do węzła lub None."""
        current_node = self.head
        while current_node is not None:
            if current_node.data == key:
                return current_node

    def display(self):
        """Wyświetl wszystkie elementy listy."""
        current_node = self.head
        while current_node is not None:
            print(f" Węzeł =  {current_node.data}")
            current_node = current_node.next

    def clear(self):
        """Usuń wszystkie węzły z listy, czyści listę."""
        self.head = None

    def size(self):
        """Zwróć liczbę węzłów w liście."""
        counter = 0
        current_node = self.head
        while current_node is not None:
            counter += 1
            current_node = current_node.next
        return counter




# Użycie klasy LinkedList
ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_end(20)
ll.insert_at_position(15, 10)  # Wstaw 15 na pozycji 1
ll.display()
print("Rozmiar listy:", ll.size())
ll.delete_from_beginning()
ll.delete_node(15)
ll.display()
ll.clear()
print("Rozmiar listy po wyczyszczeniu:", ll.size())
