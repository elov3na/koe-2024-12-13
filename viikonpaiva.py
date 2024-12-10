"""
Viikonpäivä

ISO 8601 -standardin (https://en.wikipedia.org/wiki/ISO_8601) mukaan viikonpäivät on numeroitu siten,
että maanantai on 1 ja sunnuntai 7. Tässä tehtävässä sinun tulee toteuttaa funktio nimeltä `viikonpaiva`,
joka saa parametrinaan kokonaisluvun, joka edustaa viikonpäivän numeroa 1-7. Funktion tulee palauttaa
merkkijonona viikonpäivän nimi suomeksi seuraavasti:

    - 1: "Maanantai"
    - 2: "Tiistai"
    - 3: "Keskiviikko"
    - 4: "Torstai"
    - 5: "Perjantai"
    - 6: "Lauantai"
    - 7: "Sunnuntai"

Jos funktiolle annetaan luku, joka ei ole välillä 1-7, sen tulee palauttaa tyhjä merkkijono "".

Esimerkit:

    >>> viikonpaiva(1)
    'Maanantai'

    >>> viikonpaiva(3)
    'Keskiviikko'

    >>> viikonpaiva(6)
    'Lauantai'

    >>> viikonpaiva(7)
    'Sunnuntai'

    >>> viikonpaiva(0)      # Luku ei ole välillä 1-7
    ''

    >>> viikonpaiva(8)      # Luku ei ole välillä 1-7
    ''

Huomaa, että funktiosi ei saa tulostaa mitään, vaan sen tulee palauttaa viikonpäivän nimi.


Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__ -lohkon sisään. Voit halutessasi
suorittaa yllä esitetyt doctest-testit komennolla:

python3 -m doctest --verbose viikonpaiva.py
"""


# Toteuta oma viikonpaiva-funktiosi tähän



if __name__ == "__main__":
    """
    Kirjoita mahdolliset omat testit ja kokeilut tähän lohkoon.
    Voit myös halutessasi poistaa tämän if-lohkon.
    """
