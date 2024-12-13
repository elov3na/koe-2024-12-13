"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""


def test_funktio_palauttaa_arvon_eika_tulosta(capsys):
    from joululaskuri import joululaskuri

    result = joululaskuri("13.12.2024")

    # funktion pitää palauttaa, se ei saa tulostaa
    assert type(result) == str
    assert '' == capsys.readouterr().out


def test_joulukuu_ennen_aattoa():
    from joululaskuri import joululaskuri

    result = joululaskuri("13.12.2024")
    vertaa(result, '11 yötä jouluun')

    result = joululaskuri("19.12.2024")
    vertaa(result, '5 yötä jouluun')

    result = joululaskuri("23.12.2024")
    vertaa(result, 'yksi yö jouluun')


def test_jouluaatto():
    from joululaskuri import joululaskuri

    result = joululaskuri("24.12.2024")
    vertaa(result, 'hyvää joulua!')


def test_joulu_meni_jo():
    from joululaskuri import joululaskuri

    result = joululaskuri("29.12.2024")
    vertaa(result, 'joulu meni jo')


def test_jouluun_pitka_aika():
    from joululaskuri import joululaskuri

    result = joululaskuri("15.06.2025")
    vertaa(result, 'jouluun on vielä aikaa')


def vertaa(a: str, b: str):
    assert a.lower() == b.lower()
