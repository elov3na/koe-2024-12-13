r"""
Alkukirjaimet

Tehtäväsi on toteuttaa funktio `rivien_alkukirjaimet_isoksi`. Funktio saa parametrinaan
merkkijonon, jonka jokaisen rivin ensimmäinen kirjain muutetaan isoksi kirjaimeksi.
Jos rivin ensimmäinen kirjain on jo valmiiksi iso, funktion ei tule muuttaa sitä.

Huomaa, että Pythonin merkkijonot ovat muuttumattomia, joten funktiosi tulee luoda uusi merkkijono,
jossa alkukirjaimet on muutettu isoksi. Funktion tulee palauttaa tämä uusi merkkijono.

Esimerkiksi kaksirivisellä syötteellä funktion tulee muuttaa molempien rivien ensimmäiset
kirjaimet isoiksi:

    >>> rivien_alkukirjaimet_isoksi("ohjelmointi on matka\njokainen rivi vie lähemmäs tavoitetta")
    'Ohjelmointi on matka\nJokainen rivi vie lähemmäs tavoitetta'

Seuraava merkkijono puolestaan sisältää useita rivejä, joista osan alkukirjaimet ovat jo valmiiksi isoja:

    >>> rivien_alkukirjaimet_isoksi("Eat\nSleep\ncode\nrepeat")
    'Eat\nSleep\nCode\nRepeat'

Merkkijono voi sisältää myös tyhjiä rivejä, jolloin ne säilyvät merkkijonossa muuttumattomina:

    >>> rivien_alkukirjaimet_isoksi("plan thoroughly\n\ncode carefully\n\ntest rigorously")
    'Plan thoroughly\n\nCode carefully\n\nTest rigorously'

Huomaa, että yllä olevissa esimerkeissä on käytetty rivinvaihtomerkkiä. Tämä merkki näkyy
lähdekoodissa \n-merkkijonona, mutta tulosteessa se näkyy oikeana rivinvaihtona:

    >>> tulos = rivien_alkukirjaimet_isoksi("Eat\nSleep\ncode\nrepeat")
    >>> print(tulos)
    Eat
    Sleep
    Code
    Repeat

Voit olettaa, että annetussa merkkijonossa on aina vähintään yksi rivi, mutta se voi sisältää myös
tyhjiä rivejä.


Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__ -lohkon sisään. Voit halutessasi
suorittaa yllä esitetyt doctest-testit komennolla:

python3 -m doctest --verbose alkukirjaimet.py
"""


# Toteuta funktioon tehtävänannon mukainen logiikka:
def rivien_alkukirjaimet_isoksi(teksti: str) -> str:
    return "???"


if __name__ == "__main__":
    """
    Kirjoita mahdolliset omat testit ja kokeilut tähän lohkoon.
    Voit myös halutessasi poistaa tämän if-lohkon.
    """
