def flatten(liste):
    sonuc = []
    for i in liste:
        if type(i) == list:
            alt = flatten(i)
            for j in alt:
                sonuc.append(j)
        else:
            sonuc.append(i)
    return sonuc


def ters_cevir(liste):
    sonuc = []
    for i in range(len(liste) - 1, -1, -1):
        if type(liste[i]) == list:
            sonuc.append(ters_cevir(liste[i]))
        else:
            sonuc.append(liste[i])
    return sonuc


print(flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]))
print(ters_cevir([[1, 2], [3, 4], [5, 6, 7]]))
