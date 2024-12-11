"""
Kiertävä indeksi

Tehtäväsi on toteuttaa funktio `kiertava_indeksi`, joka mahdollistaa peräkkäisten arvojen hakemisen
listalta listan rajojen yli. Käytännössä tämä tarkoittaa sitä, että jos indeksi ylittää listan pituuden,
se aloittaa laskennan listan alusta:

    >>> lista = ['piparkakut', 'joulutortut', 'suklaat', 'glögi']    # esimerkkilista

    >>> kiertava_indeksi(lista, 0)  # listan ensimmäinen indeksi
    'piparkakut'

    >>> kiertava_indeksi(lista, 3)  # 3 on esimerkkilistan viimeinen indeksi
    'glögi'

    >>> kiertava_indeksi(lista, 4)  # indeksi 4 kiertää esimerkkilistan ympäri takaisin alkuun:
    'piparkakut'


Funktiolle annettava indeksi voi olla myös niin suuri, että indeksit pyörähtävät ympäri useamman kerran:

    >>> kiertava_indeksi(lista, 1_000_000_000)
    'piparkakut'


Saman logiikan tulee toimia myös negatiivisilla indekseillä:

    >>> kiertava_indeksi(lista, -1) # listan viimeinen arvo
    'glögi'

    >>> kiertava_indeksi(lista, -5) # indeksi pyörähtää ympäri viimeiseen arvoon:
    'glögi'

    >>> kiertava_indeksi(lista, -6) # indeksi pyörähtää ympäri toiseksi viimeiseen arvoon:
    'suklaat'


Huomaa, että funktion tulee aina palauttaa arvo, eikä esimerkiksi tulostaa sitä:

    >>> kiertava_indeksi(lista, 999_999_999) == 'glögi'
    True

Voit olettaa, että funktiolle annettavassa listassa on aina vähintään yksi arvo ja että indeksit
ovat aina kelvollisia kokonaislukuja. Funktiosi tulee muuten toimia minkä pituisilla listoilla tahansa.

Vinkki: indeksin laskemisessa voi olla apua jakojäännöksestä eli "modulo"-operaattorista (%) sekä
len-funktiosta.


Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__ -lohkon sisään. Voit halutessasi
suorittaa yllä esitetyt doctest-testit komennolla:

python3 -m doctest --verbose kiertava_indeksi.py
"""


# Toteuta funktioon tehtävänannon mukainen logiikka:
def kiertava_indeksi(lista: list, indeksi: int) -> str:
    return "?"


if __name__ == "__main__":
    """
    Kirjoita mahdolliset omat testit ja kokeilut tähän lohkoon.
    Voit myös halutessasi poistaa tämän if-lohkon.
    """
