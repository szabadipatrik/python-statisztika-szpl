import tkinter as tk
from tkinter import scrolledtext
from statisztika_SZPL import szavak_szama_SZPL, karakter_szam_SZPL, atlag_szohossz_SZPL, betu_statisztika_SZPL, \
    szamjegyek_szama_SZPL


class StatisztikaAblak_SZPL:
    def __init__(self, master):
        self.master = master
        master.title("Statisztika Készítő SZPL")

        self.szoveg_bevitel = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=60, height=15)
        self.szoveg_bevitel.pack(pady=10, padx=10)

        self.keres_label = tk.Label(master,
                                    text="Kérem írjon be egy tetszőleges szöveget, hogy a betűk, szavak, számok statisztikáját számolhassuk!",
                                    fg="darkblue",
                                    font=("Helvetica", 12, "italic"))
        self.keres_label.pack(pady=(0, 5))

        self.szamitas_gomb = tk.Button(master, text="Statisztika Számítása", command=self.szamitas_vegzes_SZPL)
        self.szamitas_gomb.pack(pady=5)

        self.eredmeny_keret = tk.Frame(master)

        self.eredmeny_label = tk.Label(self.eredmeny_keret,
                                       text="Eredmények:",
                                       justify=tk.LEFT)
        self.eredmeny_label.pack(pady=10)

        self.uj_szamitas_gomb = tk.Button(self.eredmeny_keret,
                                          text="ÚJ SZÁMÍTÁS",
                                          command=self.visszaallitas_SZPL)
        self.uj_szamitas_gomb.pack(pady=5)

    def szamitas_vegzes_SZPL(self):
        szoveg = self.szoveg_bevitel.get(1.0, tk.END).strip()

        if not szoveg:
            eredmenyek = "Kérem, adjon meg szöveget a statisztikához."
            self.eredmeny_label.config(text=eredmenyek)
            return

        szavak_szama = szavak_szama_SZPL(szoveg)
        karakter_szam_szokozzel = karakter_szam_SZPL(szoveg, True)
        karakter_szam_szokoz_nelkul = karakter_szam_SZPL(szoveg, False)


        magan_szam, massal_szam = betu_statisztika_SZPL(szoveg)
        szamjegy_szam = szamjegyek_szama_SZPL(szoveg)

        eredmenyek = (
            "Eredmények:\n"
            f"  Szavak száma: {szavak_szama}\n"
            f"  Karakterek száma (összesen): {karakter_szam_szokozzel}\n"
            f"  Karakterek száma (szóközök nélkül): {karakter_szam_szokoz_nelkul}\n"
             "--- Betű Statisztika ---\n"
            f"  Magánhangzók száma: {magan_szam}\n"
            f"  Mássalhangzók száma: {massal_szam}\n"
            f"  Számjegyek száma: {szamjegy_szam}"
        )

        self.szamitas_gomb.pack_forget()
        self.keres_label.pack_forget()

        self.szoveg_bevitel.config(state=tk.DISABLED)

        self.eredmeny_label.config(text=eredmenyek)
        self.eredmeny_keret.pack()

    def visszaallitas_SZPL(self):
        self.szamitas_gomb.pack(pady=5)
        self.keres_label.pack(pady=(0, 5))

        self.eredmeny_keret.pack_forget()

        self.szoveg_bevitel.config(state=tk.NORMAL)
        self.szoveg_bevitel.delete(1.0, tk.END)

        self.eredmeny_label.config(text="Eredmények:")


if __name__ == "__main__":
    root = tk.Tk()
    app = StatisztikaAblak_SZPL(root)
    root.mainloop()