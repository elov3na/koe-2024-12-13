"""
Öitä jouluun

Kirjoita funktio oita_jouluun(paivamaara), joka laskee jäljellä olevien öiden määrän ennen jouluaattoa
funktiolle annetusta päivämäärästä lähtien. Funktion tulee käsitellä päivämäärä merkkijonona ja
palauttaa oikea tulos kokonaislukuna alla olevien sääntöjen mukaisesti.

Funktiolle annettava parametri `paivamaara` on aina merkkijono, joka on muodossa "pp.kk.vvvv", esimerkiksi "13.12.2024". Funktion palauttama arvo olisi tälle päivämäärälle 11:

    >>> oita_jouluun("13.12.2024")
    11

Jos annettu päivämäärä ei ole joulukuussa (kk != 12), tai jos jouluaatto on jo mennyt (pv > 24),
funktion tulee palauttaa luku -1:

    >>> oita_jouluun("30.12.2024")
    -1

    >>> oita_jouluun("01.11.2024")
    -1

    >>> oita_jouluun("01.01.2025")
    -1

Jos päivämäärä on juuri jouluaatto (24.12.) funktion tulee palauttaa luku 0:

    >>> oita_jouluun("24.12.2024")
    0

Muissa tapauksissa funktion tulee laskea, kuinka monta yötä jouluaattoon on. Esimerkiksi päivämäärälle "20.12.2024" oikea vastaus olisi 4.

    >>> oita_jouluun("20.12.2024")
    4

Funktiosi täytyy toimiva millä tahansa vuosiluvuilla ja laskea aina joulukuussa öitä saman vuoden jouluun:

    >>> oita_jouluun("23.12.2100")
    1

    >>> oita_jouluun("01.12.2030")
    23

Huomaa, että funktiosi ei saa tulostaa mitään, vaan sen tulee aina palauttaa kokonaisluku.

    >>> oita_jouluun("20.12.2024") == 4
    True


Vinkit:

* Päivämäärän osat voidaan pilkkoa joko pisteiden kohdalta (esim. paivamaara.split('.')) tai poimia merkkijonon osajonoina (esim. paivamaara[0:2]).

* Voit olettaa, että annettu päivämäärä on aina oikeassa muodossa ja kelvollinen.

Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__ -lohkon sisään. Voit halutessasi
suorittaa yllä esitetyt doctest-testit komennolla:

python3 -m doctest --verbose oita_jouluun.py
"""


# Toteuta oma oita_jouluun-funktiosi tähän


if __name__ == "__main__":
    """
    Kirjoita mahdolliset omat testit ja kokeilut tähän lohkoon.
    Voit myös halutessasi poistaa tämän if-lohkon.
    """
