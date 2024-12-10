"""
Kiertävä indeksi

Tehtäväsi on toteuttaa funktio `kiertava_indeksi`, joka mahdollistaa peräkkäisten arvojen hakemisen
listalta listan rajojen yli. Käytännössä tämä tarkoittaa sitä, että jos indeksi ylittää listan pituuden,
se aloittaa laskennan alusta listan alusta:

    >>> lista = ['piparkakut', 'joulutortut', 'suklaat', 'glögi']

    >>> kiertava_indeksi(lista, 0)
    'piparkakut'

    >>> kiertava_indeksi(lista, 3)
    'glögi'

    >>> kiertava_indeksi(lista, 4)  # indeksi 4 "kiertää ympäri" takaisin alkuun:
    'piparkakut'


Saman logiikan tulee toimia myös negatiivisilla indekseillä:

    >>> kiertava_indeksi(lista, -1)
    'glögi'

    >>> kiertava_indeksi(lista, -6)
    'suklaat'

Huomaa, että funktion tulee aina palauttaa arvo, eikä esimerkiksi tulostaa sitä:

    >>> kiertava_indeksi(lista, 1_000_000_000)
    'piparkakut'

Voit olettaa, että funktiolle annettavassa listassa on aina vähintään yksi arvo ja että indeksit
ovat aina kelvollisia kokonaislukuja.

Vinkki: indeksin laskemisessa voi olla apua jakojäännöksestä eli "modulo"-operaattorista (%) sekä
len-funktiosta.


Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__ -lohkon sisään. Voit halutessasi
suorittaa yllä esitetyt doctest-testit komennolla:

python3 -m doctest --verbose kiertava_indeksi.py
"""


# Toteuta funktioon tehtävänannon mukainen logiikka:
def kiertava_indeksi(lista: list, indeksi: int):
    return None


if __name__ == "__main__":
    """
    Kirjoita mahdolliset omat testit ja kokeilut tähän lohkoon.
    Voit myös halutessasi poistaa tämän if-lohkon.
    """
