# The Game of Life

Python 2022/2023 <br>
Projekt zaliczeniowy <br>
Marek Ostafin <br>

### Opis

Program implementuje jeden z pierwszych automatów 
komórkowych, wymyślony w 1970 roku przez brytyjskiego 
matematyka Johna Conwaya.

W mojej implementacji gra toczy się na skończonej płaszczyźnie,
podzielonej na kwadratowe komórki. 
Każda komórka, nie licząc leżących przy krawędziach planszy, ma ośmiu 
„sąsiadów”, czyli komórki przylegające do niej bokami i rogami. 
Komórki leżące na krawędziach mają odpowiednio mniejszą liczbę sąsiadów. 

Każda komórka może znajdować się w jednym z dwóch stanów: może być albo 
„żywa” (włączona), albo „martwa” (wyłączona). Stany komórek zmieniają się 
w pewnych jednostkach czasu. Stan wszystkich komórek w pewnej jednostce
czasu jest używany do obliczenia stanu wszystkich komórek w następnej jednostce.
Po obliczeniu wszystkie komórki zmieniają swój stan dokładnie w tym samym 
momencie. Stan komórki zależy tylko od liczby jej żywych sąsiadów.

### Obsługa programu

Po uruchomieniu programu gra jest wstrzymana - czyli statyczny wgląd
do obecnego pokolenia komórek. Pozwala to swobodnie dodawać i usuwać 
żywe komórki poprzez klikanie na nie lewym przyciskiem myszy. <br>
Grę można wznowić i ponownie wstrzymać wciskając **spację**.

Poprzez wciskanie odpowiednich przycisków dostępne są następujące akcje:

- **Spacja** : wstrzymywanie/wznawianie gry
- **+** : Przyspieszanie działania gry
- **-** : Spowalnianie działania gry
- **R** : Zaludnianie losowo części planszy
- **C** : Czyszczenie planszy
- **Q/Esc** : Zamykanie gry