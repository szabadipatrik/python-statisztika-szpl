def szavak_szama_SZPL(szoveg):
    szavak = szoveg.split()
    return len(szavak)


def karakter_szam_SZPL(szoveg, szokozt_szamol=True):
    if szokozt_szamol:
        return len(szoveg)
    else:
        szoveg_szokoz_nelkul = "".join(szoveg.split())
        return len(szoveg_szokoz_nelkul)


def atlag_szohossz_SZPL(szoveg):
    szavak = szoveg.split()
    if not szavak:
        return 0
    osszes_hossz = sum(len(szo) for szo in szavak)
    return osszes_hossz / len(szavak)


def betu_statisztika_SZPL(szoveg):
    maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
    magan_szam = 0
    massal_szam = 0

    csak_betuk = "".join(filter(str.isalpha, szoveg))

    for betu in csak_betuk:
        if betu in maganhangzok:
            magan_szam += 1
        else:
            massal_szam += 1

    return magan_szam, massal_szam