import os
from bs4 import BeautifulSoup

# Verzeichnis mit den HTML-Dateien
directory = '/Users/sby/Library/CloudStorage/OneDrive-PPIAG/korrespondenzvorlage-crossnative/templates'

# Pfad zu den Unterordnern "Deutsch" und "Englisch"
deutsch_folder = os.path.join(directory, 'Deutsch')
englisch_folder = os.path.join(directory, 'Englisch')

# Erstellen der Ordner "Deutsch" und "Englisch", falls sie nicht vorhanden sind
if not os.path.exists(deutsch_folder):
    os.makedirs(deutsch_folder)
if not os.path.exists(englisch_folder):
    os.makedirs(englisch_folder)

# Durchsuche alle Dateien im Verzeichnis
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        file_path = os.path.join(directory, filename)

        # HTML-Datei öffnen und Inhalt lesen
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # HTML-Inhalt analysieren
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text()

        # Prüfe, ob die Phrase "Best wishes," im Text vorhanden ist
        if 'Best wishes,' in text:
            # Englischer Inhalt - Datei in den "Englisch"-Ordner verschieben
            new_file_path = os.path.join(englisch_folder, filename)
            os.rename(file_path, new_file_path)
        else:
            # Deutscher Inhalt - Datei in den "Deutsch"-Ordner verschieben
            new_file_path = os.path.join(deutsch_folder, filename)
            os.rename(file_path, new_file_path)

        print(f'Datei "{filename}" wurde in den Ordner "{new_file_path.split("/")[-2]}" verschoben.')