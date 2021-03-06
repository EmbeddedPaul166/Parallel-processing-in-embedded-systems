# Podstawowe operacje na obrazach w OpenCV

## Wskazówki:

1. OpenCV wykorzystuje numpy jako backend w Pythonie. Dzięki temu wszystkie operacje na tablicach z numpy można wykorzystać do przetwarzania obrazów w OpenCV.

2. By wyświetlić obraz z kamery poprzez OpenCV, musi on być znormalizowany do przedziału 0-255 dla obrazów uint8 i 0-1 dla obrazów float32. Ramka zczytana z kamery ma typ danych uint8.

3. Zmiany kontrastu i jasności dokonuje się przez wzór: nowy_obraz = alpha * stary_obraz + beta. Alpha kontroluje zmianę kontrastu, a beta jasność. Należy pamiętać by nie zwiększyć/zmniejszyć wartości poza zakres wartości odpowiedni do wyświetlenia dla danego typu obrazu.

4. Numpy pozwala na wykonywanie operacji tylko na określonych polach w tablicy, które spełniają dany warunek. Operacja ta nazywa się maskowaniem.
    Przykład 1: pomnożenie wartości, które mają większą wartość od 100 przez 2: 2 * tablica[tablica > 100].
    Przykład 2: przypisanie wartości 0 dla wartości ujemnych w tablicy: tablica[tablica < 0] = 0

5. Wyświetlenie obrazu po ssh będzie miało niską liczbę fps. W celu uzyskania maksymalnej liczby fps, można podłączyć monitor zewnętrzny i uruchomić skrypt przekierowując wyświetlanie na niego przez ssh: DISPLAY=0 python3 video_capture.py


## Zadania:

1. Uruchom skrypt video_capture.py i zapoznaj się z jego działaniem.
2. Przekonwertuj ramkę z kamery na float32 i znormalizuj do zakresu wartości 0-1 (cv2.normalize(), NORM_MINMAX).
3. Zmodyfikuj skrypt tak, by
- dodać filtrowanie gaussowskie
- dodać filtrowanie medianowe
- dodać filtrowanie uśredniające
- wyniki wyświetlić w czasie rzeczywistym w formie okna podzielonego na cztery obrazy (zwykły obraz z kamery i 3 obrazy po filtracji, numpy.hstack(), numpy.vstack())
4. Zmodyfikuj skrypt tak, by
- zwiększyć kontrast na obrazie
- rozjaśnić obraz
- przyciemnić obraz
- wyniki wyświetl analogicznie do poprzedniego punktu

Kompletny skrypt do 3 i 4, wraz ze zrzutami ekranu z działania 3 i 4 spakować w zip i wstawić na ekursy.
