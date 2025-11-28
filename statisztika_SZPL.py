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