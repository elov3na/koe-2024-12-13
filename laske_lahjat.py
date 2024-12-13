import math

def laske_lahjat(kilttipisteet, tuhmapisteet):

    if tuhmapisteet >= (kilttipisteet * 2):
        if kilttipisteet % 2 != 0:
            kilttipisteet = kilttipisteet + 1
        return f"Lahjoja: {math.ceil(kilttipisteet / 2)} kpl"
    elif tuhmapisteet == 0:
        return f"Lahjoja: {kilttipisteet * 2} kpl"
    elif kilttipisteet == 0:
        return "Lahjoja: 1 kpl"
    else:
        return f"Lahjoja: {kilttipisteet} kpl"
    

