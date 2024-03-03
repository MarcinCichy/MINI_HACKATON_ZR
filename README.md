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

Pobranie elementu powinno zwrócić nie element 1 (jak przy tradycyjnej kolejce), ale element 3 z najwyższym priorytetem. Czyli po pobraniu, kolejka wygląda tak:

- element 1: list - priorytet 0
- element 2: list - priorytet 0
- element 3: list - priorytet 3

Jeśli w kolejce jest kilka elementów o tym samym priorytecie, powinny być zwracane w kolejności dostania się na listę. Jeśli jednak będzie to dla Ciebie teraz za trudne do zaimplementowania, zwracaj je losowo).
