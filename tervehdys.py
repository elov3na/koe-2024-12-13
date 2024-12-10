"""
Tervehdys

Toteuta funktio `tervehdi`, joka saa kaksi parametria: nimen ja kielikoodin. Funktion tulee tulostaa tervehdys
annettua koodia (fi, en, sv) vastaavalla kielellä käyttäen annettua nimeä. Tervehdyksen tulee olla eri kielillä
seuraavanlainen, jos nimeksi on annettu Emma:

- Suomeksi (fi): "Hei Emma!"
- Englanniksi (en): "Hello Emma!"
- Ruotsiksi (sv): "Hej Emma!"

Esimerkki:

    >>> tervehdi('Mirella', 'fi')
    Hei Mirella!

    >>> tervehdi('Hugo', 'en')
    Hello Hugo!

    >>> tervehdi('Anna', 'sv')
    Hej Anna!


Jos annettu kieli on tyhjä (None) tai ei mikään yllä olevista vaihtoehdoista, funktion tulee tulostaa tervehdys
englanniksi. Jos nimi puolestaan on tyhjä tyhjä tai None, funktion tulee tulostaa "Hello stranger!", riippumatta
annetusta kielikoodista.

Esimerkit:

    >>> tervehdi('James', '')       # tyhjä kieli
    Hello James!

    >>> tervehdi('James', 'de')     # tuntematon kieli
    Hello James!

    >>> tervehdi('', 'fi')          # tyhjä nimi
    Hello stranger!

    >>> tervehdi(None, 'fi')        # puuttuva nimi
    Hello stranger!

    >>> tervehdi(None, None)        # puuttuva nimi ja kieli
    Hello stranger!


Käytä print()-funktiota tervehdyksen tulostamiseksi. Tässä tehtävässä funktiosi ei saa palauttaa mitään.


Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__ -lohkon sisään. Voit halutessasi
suorittaa yllä esitetyt doctest-testit komennolla:

python3 -m doctest --verbose tervehdys.py
"""


# Toteuta oma tervehdi-funktiosi tänne



if __name__ == "__main__":
    """
    Kirjoita mahdolliset omat testit ja kokeilut tähän lohkoon.
    Voit myös halutessasi poistaa tämän if-lohkon.
    """
