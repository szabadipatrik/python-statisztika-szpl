def szavak_szama_SZPL(szoveg):
    szavak = szoveg.split()
    return len(szavak)


def karakter_szam_SZPL(szoveg, szokozzel):
    if szokozzel:
        return len(szoveg)
    else:
        karakterek = [k for k in szoveg if not k.isspace()]
        return len(karakterek)


def atlag_szohossz_SZPL(szoveg):
    szavak = szoveg.split()
    if not szavak:
        return 0.0

    # Kiszűrjük a betűket nem tartalmazó 'szavakat' (pl. csak írásjelek, vagy számok) a szóhossz számításhoz
    tisztitott_szavak = [szo for szo in szavak if any(c.isalpha() for c in szo)]

    if not tisztitott_szavak:
        return 0.0

    osszes_hossz = sum(len(szo) for szo in tisztitott_szavak)
    return osszes_hossz / len(tisztitott_szavak)


def betu_statisztika_SZPL(szoveg):
    maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
    massalhangzok = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    magan_szam = 0
    massal_szam = 0

    for karakter in szoveg:
        if karakter in maganhangzok:
            magan_szam += 1
        elif karakter in massalhangzok:
            massal_szam += 1

    return magan_szam, massal_szam


def szamjegyek_szama_SZPL(szoveg):
    szamjegy_szam = 0
    for karakter in szoveg:
        if karakter.isdigit():
            szamjegy_szam += 1
    return szamjegy_szam