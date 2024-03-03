class HashTable:
    def __init__(self, size=10):
        self.size = size
        # Inicjalizacja tablicy (będącej listą list dla obsługi kolizji metodą łańcuchową)
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        # Metoda do obliczania indeksu w tablicy dla danego klucza
        hash_key = hash(key)
        hash_table_index = hash_key % self.size
        return hash_table_index

    def find_drawer_and_index (self, key):
        index = self.hash_function(key)
        drawer = self.table[index]
        for item in drawer:
            if item[0] == key:
                return drawer, drawer.index(item)
        return drawer, None

    def insert(self, key, value):
        # Metoda do dodawania pary klucz-wartość do tablicy haszującej
        drawer, index = self.find_drawer_and_index(key)
        if index is not None:
            drawer[index] = (key, value)
        else:
            drawer.append((key, value))

    def remove(self, key):
        # Metoda do usuwania pary klucz-wartość na podstawie klucza
        drawer, index = self.find_drawer_and_index(key)
        if index is not None:
            del drawer[index]

    def search(self, key):
        # Metoda do wyszukiwania wartości na podstawie klucza
        drawer, index = self.find_drawer_and_index(key)
        if index is not None:
            return f'Value of key: {key} is {drawer[index][1]}'
        return f'The key: {key} does not exist'

    def contains(self, key):
        # Metoda do sprawdzania, czy klucz znajduje się w tablicy
        _, index = self.find_drawer_and_index(key)
        if index is None:
            return f'Key {key} not exist'
        return f'Key {key} exist'

    def count_elements(self):
        # Metoda do zwracania liczby elementów w tablicy
        return sum(len(drawer) for drawer in self.table)


# Przykład użycia (będzie wymagał implementacji metod)
hash_table = HashTable(size=10)
hash_table.insert("klucz1", "wartość1")
hash_table.insert("klucz2", "wartość2")
hash_table.insert("klucz3", "wartość3")
hash_table.insert("klucz4", "wartość4")
hash_table.insert("klucz5", "wartość5")
hash_table.insert("klucz6", "wartość6")
print(hash_table.search("klucz2"))
print(hash_table.contains("klucz5"))
print(hash_table.search("klucz5"))
hash_table.remove("klucz5")
print(hash_table.search("klucz5"))
print(hash_table.contains("klucz1"))
print(hash_table.contains("klucz8"))
print(hash_table.count_elements())
