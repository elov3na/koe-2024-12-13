"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""
import pytest


@pytest.fixture
def lista():
    return ['a', 'b', 'c', 'd', 'e']


def test_funktio_palauttaa_arvon_eika_tulosta(capsys, lista):
    from kiertava_indeksi import kiertava_indeksi

    result = kiertava_indeksi(lista, 0)

    # funktion pitää palauttaa, se ei saa tulostaa
    assert type(result) == str
    assert '' == capsys.readouterr().out


def test_normaalit_indeksit_alusta(lista):
    from kiertava_indeksi import kiertava_indeksi

    assert kiertava_indeksi(lista, 0) == lista[0]
    assert kiertava_indeksi(lista, 1) == lista[1]
    assert kiertava_indeksi(lista, 2) == lista[2]
    assert kiertava_indeksi(lista, 3) == lista[3]
    assert kiertava_indeksi(lista, 4) == lista[4]


def test_normaalit_indeksit_lopusta(lista):
    from kiertava_indeksi import kiertava_indeksi

    assert kiertava_indeksi(lista, -1) == lista[-1]
    assert kiertava_indeksi(lista, -2) == lista[-2]
    assert kiertava_indeksi(lista, -3) == lista[-3]
    assert kiertava_indeksi(lista, -4) == lista[-4]


def test_positiivinen_indeksi_kiertaa(lista):
    from kiertava_indeksi import kiertava_indeksi

    assert kiertava_indeksi(lista, 5) == lista[0]
    assert kiertava_indeksi(lista, 6) == lista[1]
    assert kiertava_indeksi(lista, 10_002) == lista[2]
    assert kiertava_indeksi(lista, 10_004) == lista[4]


def test_negatiivinen_indeksi_kiertaa(lista):
    from kiertava_indeksi import kiertava_indeksi

    assert kiertava_indeksi(lista, -6) == lista[-1]
    assert kiertava_indeksi(lista, -7) == lista[-2]
    assert kiertava_indeksi(lista, -10_001) == lista[-1]
    assert kiertava_indeksi(lista, -10_002) == lista[-2]


def vertaa(a: str, b: str):
    assert a.lower() == b.lower()
