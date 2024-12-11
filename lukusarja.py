"""
Lukusarja

Tehtäväsi on toteuttaa funktio `lukusarja`, joka saa parametrinaan positiivisen kokonaisluvun ja
muodostaa sekä palauttaa listan kokonaislukuja alla kuvailtujen sääntöjen mukaisesti.

Muodostettavan listan täytyy alkaa funktiolle annetusta luvusta ja sen täytyy päättyä ykköseen.
Ensimmäisen luvun jälkeen seuraava luku asetetaan aina seuraavien sääntöjen mukaan:

1. jos edellinen luku on parillinen, se jaetaan kahdella ja tulos lisätään listalle
2. jos edellinen luku on pariton, se kerrotaan kolmella ja tuloon lisätään yksi, ja tulos lisätään listalle.

Tätä logiikkaa toistetaan, kunnes saavutetaan luku 1.

Jos siis lukusarjan ensimmäinen luku on esimerkiksi seitsemän (pariton), seuraava luku saadaan kertomalla
7 kolmella ja lisäämällä yksi: 7 * 3 + 1 = 22. Luvusta 22 (parillinen) seuraava luku saadaan jakamalla
se kahdella, eli 22 / 2 = 11. Tätä logiikkaa jatketaan, kunnes lukusarja saavuttaa ykkösen:

7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

Lopuksi kaikki käsitellyt luvut palautetaan listana:

    >>> lukusarja(7)
    [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


Seuraavassa lyhyemmässä esimerkissä aloitetaan luvusta kahdeksan ja kaikki sarjan luvut ykköseen asti
sattuvat olemaan parillisia. Seuraava luku saaadan siis tässä aina jakamalla edellinen kahdella:

    >>> lukusarja(8)
    [8, 4, 2, 1]

Seuraavassa esimerkissä on myös parittomia lukuja, joiden tapauksessa seuraava luku saadaan kertomalla
edellinen kolmella ja lisäämällä tuloon yksi:

    >>> lukusarja(3)
    [3, 10, 5, 16, 8, 4, 2, 1]

Huomaa, että funktio ei saa tulostaa tulosta, vaan lista täytyy palauttaa paluuarvona:

    >>> lukusarja(2) == [2, 1]      # älä tulosta, vaan palauta!
    True



Voit olettaa, että funktiolle annetaan aina jokin ykköstä suurempi kokonaisluku.

Tämä tehtävä perustuu matemaattiseen, toistaiseksi todistamatta olevaan väittämään nimelta
Collatzin konjektuuri. Sen mukaan lukujono saavuttaa aina ykkösen riippumatta siitä, mistä luvusta
aloitetaan. Voit lukea lisää aiheesta esimerkiksi sivulta https://fi.wikipedia.org/wiki/Collatzin_konjektuuri.


Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__ -lohkon sisään. Voit halutessasi
suorittaa yllä esitetyt doctest-testit komennolla:

python3 -m doctest --verbose lukusarja.py
"""


# Toteuta funktioon tehtävänannon mukainen logiikka:
def lukusarja(alku: int) -> list:
    return []


if __name__ == "__main__":
    """
    Kirjoita mahdolliset omat testit ja kokeilut tähän lohkoon.
    Voit myös halutessasi poistaa tämän if-lohkon.
    """
