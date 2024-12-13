def joululaskuri(paivamaara):
    paiva = int(paivamaara[0:2])
    kuuk = int(paivamaara[3:5])

    if kuuk == 12:
        if paiva == 24:
            return "Hyvää joulua!"
        elif paiva == 23:
            return "yksi yö jouluun"
        elif paiva > 24:
            return "joulu meni jo"
        elif paiva < 23:
            return f"jouluun on {24 - paiva} yötä"
    elif kuuk != 12:
        return "jouluun on vielä aikaa"

