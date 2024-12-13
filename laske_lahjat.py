"""
Laske lahjat

Kirjoita funktio `laske_lahjat(kilttipisteet, tuhmapisteet)`, joka laskee lahjojen määrän henkilön "kilttipisteiden"
ja "tuhmapisteiden" perusteella. Funktion tulee palauttaa merkkijono, joka on muodossa "Lahjoja: X kpl", esimerkiksi
"Lahjoja: 5 kpl". Lahjojen määrä lasketaan eri tilanteissa kiltti- ja tuhmapisteiden perusteella eri tavoin, jotka
käyvät ilmi seuraavista määrittelyistä.


# Normaalitapaus

Normaalissa tapauksessa lahjojen määrä vastaa henkilön kilttipisteiden määrää:

    >>> laske_lahjat(5, 3)      # 5 kilttipistettä -> 5 lahjaa
    'Lahjoja: 5 kpl'


# Erikoistapaus 1: ei kilttipisteitä

Jos henkilöllä ei ole yhtään kilttipistettä, hän saa silti yhden lahjan.

    >>> laske_lahjat(0, 4)      # ei kilttipisteitä -> yksi lahja
    'Lahjoja: 1 kpl'


# Erikoistapaus 2: ei tuhmapisteitä

Jos henkilöllä ei ole yhtään tuhmapistettä, hän saa kilttipisteiden määrän tuplana:

    >>> laske_lahjat(3, 0)      # ei tuhmapisteitä -> tuplasti lahjoja!!!
    'Lahjoja: 6 kpl'

Jos henkilöllä ei tässä tapauksessa ole myöskään kilttipisteitä, sovelletaan
erikoistapausta 1, ja lahjoja annetaan 1 kpl:

    >>> laske_lahjat(0, 0)      # ei lainkaan pisteitä -> yksi lahja
    'Lahjoja: 1 kpl'


# Erikoistapaus 3: tuplasti tuhmapisteitä

Jos henkilöllä on vähintään kaksinkertainen määrä tuhmapisteitä kilttipisteisiin nähden, lahjojen
määrä on kilttipisteet jaettuna kahdella siten, että tulos pyöristetään ylöspäin.

    >>> laske_lahjat(4, 8)      # tuplasti tuhmapisteitä -> puolet lahjoista (pyöristystä ei tarvita)
    'Lahjoja: 2 kpl'

    >>> laske_lahjat(5, 10)     # tuplasti tuhmapisteitä -> puolet lahjoista (pyöristys ylös)
    'Lahjoja: 3 kpl'

    >>> laske_lahjat(3, 8)      # tuplasti tuhmapisteitä -> puolet lahjoista (pyöristys ylös)
    'Lahjoja: 2 kpl'



Funktiosi ei saa tulostaa mitään, vaan teksti pitää palauttaa paluuarvona:

    >>> laske_lahjat(3, 5) == 'Lahjoja: 3 kpl'
    True

    >>> laske_lahjat(0, 10_000_000_000_000_000) == 'Lahjoja: 1 kpl'
    True


# Vinkkejä

- voit olettaa, että sekä `kilttipisteet` että `tuhmapisteet` ovat kokonaislukuja ja vähintään nollia.
- Pythonin `math.ceil`-funktio voi auttaa ylöspäin pyöristämisessä


Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__ -lohkon sisään. Voit halutessasi
suorittaa yllä esitetyt doctest-testit komennolla:

python3 -m doctest --verbose laske_lahjat.py
"""

# Toteuta oma laske_lahjat-funktiosi tähän


if __name__ == "__main__":
    """
    Kirjoita mahdolliset omat testit ja kokeilut tähän lohkoon.
    Voit myös halutessasi poistaa tämän if-lohkon.
    """
