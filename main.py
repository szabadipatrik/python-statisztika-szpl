import tkinter as tk
from tkinter import scrolledtext
from statisztika_SZPL import szavak_szama_SZPL, karakter_szam_SZPL, atlag_szohossz_SZPL


class StatisztikaAblak_SZPL:
    def __init__(self, master):
        self.master = master
        master.title("Statisztika Készítő SZPL")

        self.szoveg_bevitel = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=60, height=15)
        self.szoveg_bevitel.pack(pady=10, padx=10)

        self.szamitas_gomb = tk.Button(master, text="Statisztika Számítása", command=self.szamitas_vegzes_SZPL)
        self.szamitas_gomb.pack(pady=5)

        self.eredmeny_label = tk.Label(master, text="Eredmények:\nKérem, írjon be szöveget...", justify=tk.LEFT)
        self.eredmeny_label.pack(pady=10)

    def szamitas_vegzes_SZPL(self):
        szoveg = self.szoveg_bevitel.get(1.0, tk.END).strip()

        if not szoveg:
            eredmenyek = "Kérem, adjon meg szöveget a statisztikához."
        else:
            szavak_szama = szavak_szama_SZPL(szoveg)
            karakter_szam_szokozzel = karakter_szam_SZPL(szoveg, True)
            karakter_szam_szokoz_nelkul = karakter_szam_SZPL(szoveg, False)
            atlag_szohossz = atlag_szohossz_SZPL(szoveg)

            eredmenyek = (
                "Eredmények:\n"
                f"  Szavak száma: {szavak_szama}\n"
                f"  Karakterek száma (szóközökkel): {karakter_szam_szokozzel}\n"
                f"  Karakterek száma (szóközök nélkül): {karakter_szam_szokoz_nelkul}\n"
                f"  Átlagos szóhossz: {atlag_szohossz:.2f}"
            )

        self.eredmeny_label.config(text=eredmenyek)


if __name__ == "__main__":
    root = tk.Tk()
    app = StatisztikaAblak_SZPL(root)
    root.mainloop()