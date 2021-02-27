# Trening podstawowej konwolucyjnej sieci neuronowej w keras (tensorflow)

## Wskazówki:

1. Keras jest wbudowany w tensorflow i pełni rolę wysokopoziomowego API do tworzenia sieci neuronowych.

2. W procesie treningu sieci najważniejszym elementem jest zbiór danych. Zbiór ten w trakcie treningu dzielimy na:
- zbiór treningowy: część zbioru, która bierze udział w uczeniu sieci, zwykle jest to 60-80% całego zbioru danych.
- zbiór walidacyjny: część zbioru służąca do ewaluacji performance'u modelu co każdą epokę (iterację) treningową, zwykle 10-20% całego zbioru danych. Taka ewaluacja odbywa się cyklicznie w trakcie procesu treningu. Jej głównym zadaniem jest sprawdzanie, czy model poprawia swoją skuteczność na danych, które nie zostały użyte w procesie treningu (których nigdy nie widział).
- zbiór testowy: część zbioru służąca do ostatecznej ewaluacji modelu po skończonym procesie treningowym, zwykle 10-20% całego zbioru danych.

3. W niektórych przypadkach konieczna jest obróbka zbioru danych poprzez różne techniki augmentacji: przekształcenia, przesunięcia elementów na obrazie, obroty, zaszumianie. Głównym celem augmentacji jest sprawienie, by model poprzez naukę na danym zbiorze potrafił odpowiednio uogólniać swoje predykcje i nie polegać zbyt mocno na detalach w zbiorze uczącym. Jest to również jedna z technik walki z overfittingiem.

4. Jako częste problemy w treningu sieci neuronowych wyróżnia się:
- Overfitting: można go poznać po tym, że celność treningowa rośnie co epokę, a celność walidacyjna spada, lub utrzymuje się na tym samym poziomie, co skutkuje powiększaniem się różnicy między celnościami. 
- Underfitting: ma miejsce, gdy zarówno celność treningowa jak i walidacyjna nie rosną, spadają lub rosną bardzo wolno na przestrzeni epok treningowych.

O technikach walki z overfittingiem i underfittingiem będzie na kolejnych laboratoriach.

5. Tensorboard to narzędzie służące do analizy procesu uczenia sieci. Pozwala sprawdzić m.in. przebieg celności na przestrzeni epok i histogramy wag w każdej warstwie sieci. 

## Zadania:

1. Wejść na https://www.tensorflow.org/tutorials/images/cnn?hl=en i przerobić cały tutorial. Dotyczy on klasyfikacji obrazów w zbiorze CIFAR.
2. Wejść na https://www.tensorflow.org/tensorboard/get_started i według sekcji "Using TensorBoard with Keras Model.fit()" dodać generację logów tensorboard do poprzedniej klasyfikacji. Po tym ponownie przeprowadzić trening sieci i uruchomić tensorboard.

Na ekursy należy wstawić spakowane:
- wynikowy skrypt w pythonie
- hash pliku modelu (używając programu md5sum na pliku modelu)
- screeny ze zmian histogramów w poszczególnych warstwach modelu po przeprowadzeniu treningu
- screen ze zmian celności na przestrzeni epok


