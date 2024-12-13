"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""


def test_funktio_palauttaa_arvon_eika_tulosta(capsys):
    from laske_lahjat import laske_lahjat

    result = laske_lahjat(0, 0)

    # funktion pitää palauttaa, se ei saa tulostaa
    assert type(result) == str
    assert '' == capsys.readouterr().out


def test_normaalitapaus():
    from laske_lahjat import laske_lahjat

    result = laske_lahjat(10, 3)
    vertaa(result, 'Lahjoja: 10 kpl')


def test_ei_kilttipisteitä():
    from laske_lahjat import laske_lahjat

    result = laske_lahjat(0, 3)
    vertaa(result, 'Lahjoja: 1 kpl')


def test_ei_tuhmapisteita():
    from laske_lahjat import laske_lahjat

    result = laske_lahjat(3, 0)
    vertaa(result, 'Lahjoja: 6 kpl')


def test_tuplasti_tuhmapisteita():
    from laske_lahjat import laske_lahjat

    result = laske_lahjat(2, 4)
    vertaa(result, 'Lahjoja: 1 kpl')

    result = laske_lahjat(11, 100)
    vertaa(result, 'Lahjoja: 6 kpl')

    result = laske_lahjat(13, 100)
    vertaa(result, 'Lahjoja: 7 kpl')


def vertaa(a: str, b: str):
    assert a.lower() == b.lower()
