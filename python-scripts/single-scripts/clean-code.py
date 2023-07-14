import os
from bs4 import BeautifulSoup

# Pfad zum Verzeichnis mit den HTML-Mailvorlagen
verzeichnis_pfad = "/Users/sby/Library/CloudStorage/OneDrive-PPIAG/korrespondenzvorlage-crossnative/templates"

def ordne_vorlagen(verzeichnis_pfad):
    for datei_name in os.listdir(verzeichnis_pfad):
        if datei_name.endswith(".html"):
            datei_pfad = os.path.join(verzeichnis_pfad, datei_name)
            # HTML-Datei öffnen und den Inhalt lesen
            with open(datei_pfad, "r") as datei:
                inhalt = datei.read()

            # HTML-Code aufräumen und optimieren
            soup = BeautifulSoup(inhalt, "html.parser")
            optimierter_code = soup.prettify()

            # Optimierten Code in die Datei schreiben
            with open(datei_pfad, "w") as datei:
                datei.write(optimierter_code)

            print(f"Vorlage {datei_name} wurde optimiert.")

    print("Alle Vorlagen wurden optimiert.")

# Aufruf der Funktion zum Ordnen, Aufräumen und Optimieren der Vorlagen
ordne_vorlagen(verzeichnis_pfad)