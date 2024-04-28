***** Spotkanie 002 - HASH TABLE  *****
Tablica haszująca (HashTable) jest strukturą danych, która umożliwia szybkie wyszukiwanie, wstawianie i usuwanie elementów na podstawie kluczy. W Pythonie, ta struktura jest bardzo podobna do wbudowanego słownika (**`dict`**), ale celem tego zadania jest stworzenie własnej implementacji tablicy haszującej.

**Podstawowe metody tablicy haszującej (które należy zaimplementować w ramach rozwiązania):**

- **Dodaj element:** Wstawia parę klucz-wartość do tablicy. Jeśli klucz już istnieje, aktualizuje jego wartość.
- **Usuń element:** Usuwa parę klucz-wartość na podstawie podanego klucza.
- **Pobierz wartość:** Zwraca wartość skojarzoną z podanym kluczem. Jeśli klucz nie istnieje, zwraca **`None`** lub inny określony komunikat.
- **Czy zawiera klucz?** Sprawdza, czy dany klucz istnieje w tablicy haszującej.
- **Ile elementów jest w tablicy:** Zwraca liczbę elementów przechowywanych w tablicy haszującej.

**Twoim zadaniem jest stworzyć samemu implementację tablicy haszującej.**

W Twojej implementacji powinieneś użyć prostej metody haszującej (hash - w kolejnym akapicie znajdziesz przykłady), np. reszty z dzielenia (**`mod`**) haszu klucza (hash) przez rozmiar tablicy, aby określić, gdzie umieścić parę klucz-wartość. Do obsługi kolizji (sytuacji, gdy dwa klucze mają ten sam hasz), możesz użyć jednej z dwóch metod: łańcuchowej (przechowywanie listy elementów w każdej komórce tablicy) lub otwartego adresowania (znalezienie innego miejsca w tablicy, jeśli miejsce jest już zajęte).


***** Spotkanie 001 - KOLEJKA PRIORYTETOWA *****

Klasyczna kolejka (Queue), emuluje działanie “tradycyjnej” kolejki jaką spotkasz np. w sklepie czy kinie. Ustawiasz się na końcu i przesuwasz do przodu aż ktoś Cię obsłuży.

Podstawowe metody kolejki (**które należy zaimplementować w ramach rozwiązania**):

- Dodaj element na końcu kolejki
- Pobierz i usuń element z początku kolejki
- Pobierz 1 element bez usuwania (podgląd)
- Czy kolejka jest pusta?
- Ile elementów jest w kolejce

**Twoim zadaniem jest stworzyć samemu implementację  kolejki… priorytetowej.**

Różni się od tradycyjnej kolejki tym, że oprócz elementu z danymi jest jeszcze priorytet. Elementy o wyższym priorytecie wychodzą z kolejki przed elementami o niższym priorytecie.

Przykład:

- element 1: list - priorytet 0
- element 2: list - priorytet 0
- element 3: list - priorytet 5
- element 4: list - priorytet 3

Pobranie elementu powinno zwrócić nie element 1 (jak przy tradycyjnej kolejce), ale element 3 z najwyższym priorytetem. 
Czyli po pobraniu, kolejka wygląda tak:

- element 1: list - priorytet 0
- element 2: list - priorytet 0
- element 3: list - priorytet 3

Jeśli w kolejce jest kilka elementów o tym samym priorytecie, powinny być zwracane w kolejności dostania się na listę. 
Jeśli jednak będzie to dla Ciebie teraz za trudne do zaimplementowania, zwracaj je losowo).


***** Spotkanie 003 - LINKED LIST  *****
Linked List, czyli lista łączona, to struktura danych składająca się z serii elementów, zwanych węzłami, które są 
ze sobą połączone za pomocą odniesień (**referencji** lub **wskaźników**) do następnych węzłów w sekwencji. Każdy węzeł 
w typowej liście łączonej przechowuje dwie rzeczy: wartość (lub dane) oraz referencję do następnego węzła w liście.

Oto główne cechy listy łączonej:

- **Dynamiczna struktura danych**: Lista łączona może dynamicznie rosnąć i zmniejszać się, dodając lub usuwając węzły, 
    bez potrzeby deklarowania stałego rozmiaru z góry.
- **Efektywna manipulacja**: Operacje takie jak wstawianie i usuwanie węzłów są zazwyczaj bardziej efektywne niż 
    w tablicach, ponieważ nie wymagają przesuwania elementów.
- **Sekwencyjny dostęp**: Aby dostać się do konkretnego węzła, musisz przejść przez poprzednie węzły, zaczynając 
    od początku listy, co może być mniej wydajne niż bezpośredni dostęp oferowany przez tablice.

Listy łączone mogą przyjmować różne formy, takie jak lista jednokierunkowa (gdzie każdy węzeł wskazuje na następny), 
lista dwukierunkowa (gdzie węzły mają odniesienia zarówno do następnych, jak i poprzednich węzłów) oraz lista cykliczna 
(gdzie ostatni węzeł wskazuje z powrotem na pierwszy węzeł, tworząc cykl). Każda z tych form ma swoje zastosowania 
w zależności od wymagań konkretnej aplikacji.

👉 **Referencja** to odniesienie lub alias do już istniejącej zmiennej lub obiektu w pamięci. Kiedy operujesz 
na referencji, wpływasz bezpośrednio na obiekt, do którego się odnosi. Referencje umożliwiają pracę z danymi 
bez konieczności kopiowania ich wartości, co jest szczególnie użyteczne w przypadku dużych obiektów lub złożonych 
struktur danych. W wielu językach programowania, jak Java czy Python, referencje są automatycznie zarządzane 
przez środowisko wykonawcze, co upraszcza pisanie kodu i zarządzanie pamięcią.

**Wskaźnik** to zmienna, która przechowuje adres pamięci, gdzie znajduje się wartość lub inna zmienna. 
Umożliwia bezpośredni dostęp i manipulację danych znajdujących się pod tym adresem. Wskaźniki są bardzo użyteczne 
w niskopoziomowym programowaniu, pozwalając na efektywne i elastyczne zarządzanie pamięcią, co jest kluczowe 
w systemach operacyjnych, sterownikach urządzeń i innych aplikacjach wymagających bezpośredniego dostępu do sprzętu. 
Wskaźniki oferują programiście możliwość kontroli nad strukturami danych, alokacją pamięci i interfejsami sprzętowymi.

**Podstawowe operacje na liście łączonej - jednokierunkowej (które należy zaimplementować):**

1. **Wstawianie (Insert)**:
    - **Na początek listy**: Dodanie nowego węzła na początku listy, który staje się nową głową.
    - **Na koniec listy**: Dodanie nowego węzła na końcu listy.
    - **W środku listy**: Wstawienie nowego węzła po określonym węźle lub na konkretnej pozycji.
2. **Usuwanie (Delete)**:
    - **Z początku listy**: Usunięcie węzła z początku listy.
    - **Z końca listy**: Usunięcie węzła z końca listy, co wymaga przejścia przez całą listę do przedostatniego węzła.
    - **Określonego węzła**: Usunięcie węzła, który zawiera określone dane lub znajduje się na określonej pozycji.
3. **Wyszukiwanie (Search)**:
    - Przeszukiwanie listy w celu znalezienia węzła zawierającego określone dane lub sprawdzenie, czy dana wartość istnieje w liście.
4. **Wyświetlanie (Display)**:
    - Przejście przez wszystkie węzły listy, zwykle w celu wyświetlenia ich wartości.
5. **Czyszczenie (Clear)**:
    - Usunięcie wszystkich węzłów z listy, co efektywnie czyści listę, czyniąc ją pustą.
6. **Zwracanie rozmiaru (Size)**:
    - Zliczanie i zwracanie liczby węzłów w liście.

Te operacje umożliwiają efektywne zarządzanie danymi w liście jednokierunkowej, każda z nich ma swoje specyficzne 
zastosowania w zależności od potrzeb aplikacji. Implementacja tych operacji zapewnia podstawową funkcjonalność potrzebną 
do manipulowania danymi w strukturze listy łączonej.

Pusta lista, powinna mieć wartość None / null. Podobnie jak ostatni element listy powinien mieć wartość None / null