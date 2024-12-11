"""
Joululaskuri

Kirjoita funktio `joululaskuri(paivamaara)`, joka laskee jäljellä olevien öiden määrän ennen jouluaattoa
funktiolle annetusta päivämäärästä lähtien.

Funktiolle annettava parametri `paivamaara` on aina merkkijono, joka on muodossa "pp.kk.vvvv",
esimerkiksi "13.12.2024". Funktion tulee hyödyntää annettua päivämäärää ja palauttaa teksti alla olevien
sääntöjen mukaisesti:


# Joulukuun päivät ennen jouluaattoa (1.-23.12.)

Joulukuussa ennen jouluaattoa funktion tulee palauttaa merkkijono, jossa kerrotaan montako yötä
jouluaattoon on jäljellä. Jos öitä on vain yksi, paluuarvo on "yksi yö jouluun":

    "X yötä jouluun" (normaalitapaus, esim. "11 yötä jouluun")
    "yksi yö jouluun" (erikoistapaus, kun jouluun on 1 yö)

Esimerkit:

    >>> joululaskuri("13.12.2024")
    '11 yötä jouluun'

    >>> joululaskuri("23.12.2024")  # erikoistapaus: yksi yö jouluun
    'yksi yö jouluun'


# Jouluaatto

Jos funktiolle annettu päivämäärä on jouluaatto (24.12.), tulee funktion palauttaa teksti "hyvää joulua!"

    >>> joululaskuri("24.12.2024")  # jouluaatto
    'hyvää joulua!'


# Joulukuun päivät jouluaaton jälkeen (25.-31.12.)

Jos funktiolle annettu päivämäärä on joulukuussa jouluaaton jälkeen, tulee funktion palauttaa
teksti "joulu meni jo".

    >>> joululaskuri("26.12.2024")
    'joulu meni jo'

    >>> joululaskuri("31.12.2024")
    'joulu meni jo'


# Muut kuukaudet (joulukuun ulkopuolella)

Jos annettu päivämäärä ei ole joulukuussa, funktion tulee palauttaa teksti "jouluun on vielä aikaa".

    >>> joululaskuri("01.01.2025")
    'jouluun on vielä aikaa'

    >>> joululaskuri("15.06.2025")
    'jouluun on vielä aikaa'


Funktiosi täytyy toimiva millä tahansa vuosiluvuilla ja laskea aina joulukuussa öitä annetun
vuoden jouluaattoon:

    >>> joululaskuri("20.12.2024")
    '4 yötä jouluun'

    >>> joululaskuri("01.12.2130")
    '23 yötä jouluun'


Huomaa, että funktiosi ei saa tulostaa mitään, vaan sen tulee aina palauttaa kokonaisluku.

    >>> joululaskuri("20.12.2024") == '4 yötä jouluun'      # palauta teksti, älä tulosta mitään
    True


Vinkit:

* Päivämäärän osat voidaan pilkkoa joko pisteiden kohdalta (esim. paivamaara.split('.')) tai poimia
  merkkijonon osajonoina (esim. paivamaara[0:2]).

* Voit olettaa, että annettu päivämäärä on aina oikeassa muodossa ja kelvollinen.

Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__ -lohkon sisään. Voit halutessasi
suorittaa yllä esitetyt doctest-testit komennolla:

python3 -m doctest --verbose joululaskuri.py
"""


# Toteuta oma joululaskuri-funktiosi tähän


if __name__ == "__main__":
    """
    Kirjoita mahdolliset omat testit ja kokeilut tähän lohkoon.
    Voit myös halutessasi poistaa tämän if-lohkon.
    """
