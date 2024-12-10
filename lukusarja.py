"""
Lukusarja

Tehtäväsi on toteuttaa funktio `lukusarja`, joka saa parametrinaan positiivisen kokonaisluvun ja
muodostaa sekä palauttaa listan kokonaislukuja alla kuvailtujen sääntöjen mukaisesti.

Lista alkaa aina funktiolle annetusta luvusta ja se päättyy ykköseen. Annetusta luvusta lähtien
listan seuraava luku määräytyy aina seuraavien sääntöjen mukaan:

1. jos edellinen luku on parillinen, se jaetaan kahdella
2. jos edellinen luku on pariton, se kerrotaan kolmella ja tuloon lisätään yksi.

Jos siis lukusarjan ensimmäinen luku on esimerkiksi seitsemän, seuraava luku saadaan kertomalla
7 kolmella ja lisäämällä yksi: 7 * 3 + 1 = 22. Jos lukusarjan edellinen luku on puolestaan 22,
saadaan seuraava luku jakamalla tämä luku kahdella 22 / 2 = 11.

Tätä logiikkaa jatketaan, kunnes lukusarja saavuttaa ykkösen. Lopuksi kaikki käsitellyt luvut
palautetaan listana.

Seuraavassa esimerkissä aloitetaan luvusta kahdeksan ja kaikki sarjan luvut ykköseen asti sattuvat
olemaan parillisia. Seuraava luku saaadan siis tässä aina jakamalla edellinen kahdella:

    >>> lukusarja(8)
    [8, 4, 2, 1]

Seuraavissa esimerkeissä on myös parittomia lukuja, joiden tapauksessa seuraava luku saadaan kertomalla
luku kolmella ja lisäämällä tuloon yksi:

    >>> lukusarja(3)
    [3, 10, 5, 16, 8, 4, 2, 1]

    >>> lukusarja(7)
    [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

Huomaa, että funktio ei saa tulostaa tulosta, vaan lista täytyy palauttaa paluuarvona:

    >>> lukusarja(3) == [3, 10, 5, 16, 8, 4, 2, 1]
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
