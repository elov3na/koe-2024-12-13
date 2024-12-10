"""
Puuttuva kirjain

Tehtäväsi on toteuttaa funktio `etsi_puuttuva_kirjain`, joka etsii ja palauttaa
puuttuvan kirjaimen annetusta aakkosjärjestyksessä olevasta merkkijonosta.

Annettu merkkijono koostuu aina peräkkäisistä pienistä kirjaimista a-z, mutta yksi
kirjain puuttuu välistä:

* "abde": c puuttuu välistä
* "ac": b puuttuu välistä

Merkkijono voi alkaa ja päättyä mistä vain kohtaa aakkosia, mutta sen kirjaimet ovat
aina keskenään aakkosjärjestyksessä, eikä sama kirjain esiinny kahdesti. Esimerkiksi
seuraavat merkkijonot ovat mahdollisia:

* "efgijk": h puuttuu välistä
* "stvw": u puuttuu välistä

Funktiosi käytön tulee noudattaa seuraavaa esimerkkiä:

        >>> etsi_puuttuva_kirjain("abce")
        'd'

Huomaa, että puuttuva kirjain palautetaan, eikä esimerkiksi tulosteta. Annettava merkkijono
ei välttämättä ala kirjaimesta 'a'. Esimerkiksi seuraavasta merkkijonosta puuttuu kirjain 'f':

    >>> etsi_puuttuva_kirjain("eghijklmn")
    'f'

    >>> etsi_puuttuva_kirjain("stuvwyz")
    'x'

Voit olettaa, että annetussa merkkijonossa on aina vähintään kaksi kirjainta ja että
annetut merkkijonot noudattavat tehtävänannossa kuvailtua logiikkaa. Kirjain ei voi
koskaan puuttua annetun merkkijonon alusta eikä lopusta.


Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__ -lohkon sisään. Voit halutessasi
suorittaa yllä esitetyt doctest-testit komennolla:

python3 -m doctest --verbose puuttuva_kirjain.py
"""


# Toteuta funktioon tehtävänannon mukainen logiikka:
def etsi_puuttuva_kirjain(merkkijono: str) -> str:
    return "???"


if __name__ == "__main__":
    """
    Kirjoita mahdolliset omat testit ja kokeilut tähän lohkoon.
    Voit myös halutessasi poistaa tämän if-lohkon.

    Jos tarvitset käyttöösi aakkosten kirjaimet a-z, voit käyttää Pythonin string-moduulin
    tarjoamaa ascii_lowercase-muuttujaa. Voit ottaa sen käyttöön seuraavasti:

        import string
        aakkoset = string.ascii_lowercase   # "abcdefghijklmnopqrstuvwxyz"
    """

