"""
Pobierz z sieci plik csv. Wybierz z csv jakies kolumny i zapisz to w osobnym pliku.

"""
import csv
with open ("Baza_teleadresowa_jst_stan_na_28.02.2020.csv") as f:
    reader = csv.DictReader(f, delimiter= ";")
    dane = []
    for row in reader:
        dane.append((row["Kod_TERYT"], row["telefon kierunkowy"] + row["telefon"].replace(" ", "").replace("\n", "")))

with open("dne_out.csv", "w", newline= "") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["TERYT", "TELEFON"])
    writer.writerows(dane)