Szövegmezőbe beírt betűK, szavak, számok darabszámát számolja meg, és írja ki a szövegmező alá. 
Megszámolja a mással és magánhangzókat külön, és ezt is kiírja.

Készítette: 
Szabadi Patrik László
X66V18

Az alkalmazás két fő Phyton fájlból és a hozzájuk tartozó modulokból áll.

1.main.py a fő alkalmazás
tkinter as tk Egy grafikus felhasználói felület létrehozása
tkinetr.scrolledtext Görgős szövegbeviteli mezőkezelő
statisztika_SZPL az egyéni modul, amiben matematikai számítások vannak.

StatisztikaAblak_SZPL az alkalmazás fő osztálya. Program logika és a grafikus kezelés
init a beviteli gombok, cimkék inicializálása
szamitas_vegzes_SZPL Szövegbeolvasás,függvényhívás, eredmény kiírás
visszaallitas_SZPL újra számolás lehetősége


2.statisztika_SZPL.py /statisztikai számítások
szavak_szama_SZPL kiszámítja és visszaadja a szövegből a szavak számát
karakter_szam_SZPL Karaktereket számolja 
betu_statisztika_SZPL a mással és magánhangzók megszámolása
szamjegyek_szama_SZPL a számokat és külön megszámoljuk

A program indításához futtassuk a main.py fájlt.

