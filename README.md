### Modulacje Phase Shift Keying (PSK)

Projekt dotyczący modulacji PSK

## Spis treści
* [Opis](#opis)
* [Technologie](#technologie)
* [Uruchomienie](#uruchomienie)
* [Autorzy](#autorzy)
 
 ## Opis
 Projekt ten został stworzony w ramach kursu Niezawodność i Diagnostyka Układów Cyfrowych (NiDUC).
 Jego głównym założeniem jest zasymulowanie różnych rodzajów modulacji sygnałów.
 Na podstawie wyników zebranych podczas symulacji analizowana będzie odporność na zakłócenia danej modulacji,
 w zależności od ilości przesyłanych bitów oraz częstotliwości fal nośnych.
 Modulacje omawiane w tym projekcie to:
 * Binary Phase Shift Keying (BPSK)
 * Quadrature Phase Shift Keying (QPSK)
 * Amplitude Shift Keying (ASK)

Cały projekt składa się z dwóch części. Pierwszą z nich jest moduł `psk-simulator`, w którego skład wchodzą klasy i funkcję odpowiedzialne za symulację modulacji fazowych sygnałów. Druga część składa się z notatników, w których zaprezentowano wyniki symulacji.

 ## Technologie
Projekt został napisany w całości w języku Python 3 z następującymi bibliotekami
* `matplotlib==3.9.1`
* `numpy==2.0.1`
* `pandas==2.2.2`
* `seaborn==0.13.2`

## Uruchomienie
Aby lokalnie uruchomić projekt, najpierw należy sklonować repozytorium

```bash
git clone https://github.com/Barionetta/phase-shift-keying.git
```
Następnie stworzyć wirtualne środowisko ( tutaj pokazane na przykładzie condy )

```bash
conda create --name psk-env
```

Później należy aktywować środowisko

```bash
conda activate psk-env
```

Na końcu zainstalować wymagane paczki
```bash
pip install -e .
```

Aby odinstalować projekt, należy użyć następującej komendy
```bash
pip uninstall psksimulator
```

## Autorzy
Autorami projektu są Miłosz Siemiński i Katarzyna Matuszek
