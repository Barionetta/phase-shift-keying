### Modulacje Phase Shift Keying (PSK)
## Spis treści
* [Opis](#opis)
* [Technologie](#technologie)
* [Uruchomienie] (#uruchomienie)
* [Autorzy] (#autorzy)
 
 ## Opis
 Projekt ten został stworzony w ramach kursu Niezawodność i Diagnostyka Układów Cyfrowych (NiDUC).
 Jego głównym założeniem jest zasymulowanie różnych rodzajów modulacji sygnałów.
 Modulacje omawiane w tym projekcie to:
 * Binary Phase Shift Keying (BPSK)
 * Quadrature Phase Shift Keying (QPSK)
 * Amplitude Shift Keying (ASK)
 Na podstawie wyników zebranych podczas symulacji analizowana będzie odporność na zakłócenia danej modulacji,
 w zależności od ilości przesyłanych bitów oraz częstotliwości fal nośnych.

 ## Technologie
Projekt został napisany w całości w języku Python 3 z następującymi bibliotekami
* matplotlib==3.7.1
* numpy==1.24.3
* pandas==2.0.1
* scipy==1.10.1
* seaborn==0.12.2

## Uruchomienie
Aby lokalnie uruchomić projekt, najpierw należy sklonować repozytorium

``` bash
git clone https://github.com/Raganella/phase-shift-keying.git
```
Następnie zainstalować wymagane biblioteki

```bash
pip install -r requirements.txt
```
Uruchomić kod
```bash
python main.py
```

## Autorzy
Autorami projektu są Miłosz Siemiński i Katarzyna Matuszek