r"""
Sanahaku

Kirjoita funktio `sanahaku(sana, ruudukko)`, joka tarkistaa, löytyykö annettu sana merkkijonoruudukosta.
Sanan tulee löytyä ruudukosta joko etu- tai takaperin sekä ylhäältä alas tai alhaalta ylös.

Huom! Tässä tehtävässä on sekä suoraviivaisia osia että edistyneempiä soveltamista vaativia osia.
Arvioinnissa huomioidaan myös osittain toimivat ratkaisut, eli saat pisteitä oikein toimivista
ominaisuuksista, vaikka koko funktio ei olisikaan täysin oikein tai valmis.


# Parametrit

1. Parametri `sana` on etsittävä merkkijono, kuten "joulu".

2. Parametri `ruudukko` on monirivinen merkkijono, jossa rivit erotetaan rivinvaihtomerkeillä ("\n").
   Esimerkiksi:

   joulu
   ikkat
   ilout
   matto
   ahsap

   >>> ruudukko = "joulu\nikkat\nilout\nmatto\nahsap"  # sama ruudukko Python-merkkijonona

Funktion tulee palauttaa arvo `True`, jos sana löytyy mistä tahansa yllä mainitusta suunnasta.
Esimerkiksi yllä olevasta ruudukosta löytyy vaakasuoraan etuperin mm. sanat "joulu" ja "matto":

   >>> sanahaku("joulu", ruudukko)  # ylin rivi
   True
   >>> sanahaku("matto", ruudukko)  # neljänneksi ylin rivi
   True

Samasta esimerkkiruudukosta löytyy oikealta vasemmalle mm. sanat "takki" ja "tuoli":

   >>> sanahaku("takki", ruudukko)  # toinen rivi oikealta vasemmalle
   True
   >>> sanahaku("tuoli", ruudukko)  # kolmas rivi oikealta vasemmalle
   True

Pystysuoraan ylhäältä alas puolestaan esimerkkiruudukosta löytyy sana "lauta" ja alhaalta ylös
löytyy sanat "halko" ja "pottu":

   >>> sanahaku("lauta", ruudukko)  # neljäs pystyrivi ylhäältä alas
   True
   >>> sanahaku("halko", ruudukko)  # toinen pystyrivi alhaalta ylös
   True

Huomaa, että sanat eivät välttämättä ulotu ruudukon laidasta laitaan, vaan tästä ruudukosta
löytyisi myös lyhyempiä sanoja, kuten "oulu" ja "ilo".

   >>> sanahaku("oulu", ruudukko)   # ylin rivi
   True
   >>> sanahaku("ilo", ruudukko)    # kolmas rivi
   True

Vastaavasti funktion tulee palauttaa `False`, jos sanaa ei löydy ruudukosta:

   >>> sanahaku("bolero", ruudukko)
   False
   >>> sanahaku("nahkatakki", ruudukko)
   False


# Vinkit

- Voit olettaa, että kaikki rivit ovat yhtä pitkiä, eli ruudukko on nelikulmio.
- Voit olettaa, että ruudukon koko on aina vähintään 2x2 kirjainta.
- Voit olettaa, että sekä annettu sana että sanaruudukko sisältävät vain pieniä kirjaimia.
- Sana voi esiintyä vaakarivillä vasemmalta oikealle tai oikealta vasemmalle.
- Sana voi esiintyä pystyrivillä ylhäältä alas tai alhaalta ylös.
- Sanoja ei etsitä vinoista suunnista.
- Funktio ei saa tulostaa mitään, vaan sen tulee palauttaa totuusarvo True False.
- Voit olettaa, että annetut parametrit ovat aina oikeassa muodossa ja kelvollisia.
- Tehtävässä voi olla apua mm. `splitlines()`-metodista sekä merkkijonon kääntämisestä (`[::-1]`).


Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__ -lohkon sisään. Voit halutessasi
suorittaa yllä esitetyt doctest-testit komennolla:

python3 -m doctest --verbose sanahaku.py
"""


def sanahaku(sana: str, ruudukko: str) -> bool:
    # Toteuta oma funktiosi tähän
    return False


if __name__ == "__main__":
    """
    Kirjoita mahdolliset omat testit ja kokeilut tähän lohkoon.
    Voit myös halutessasi poistaa tämän if-lohkon.
    """
