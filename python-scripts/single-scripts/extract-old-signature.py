import os

directory = '/Users/sby/Library/CloudStorage/OneDrive-PPIAG/korrespondenzvorlage-crossnative/templates'

# Durch das Verzeichnis mit HTML-Vorlagen iterieren
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        file_path = os.path.join(directory, filename)

        # HTML-Vorlage öffnen und den Inhalt lesen
        with open(file_path, 'r') as file:
            content = file.read()

        # Den gewünschten Text finden und den Teil ab diesem Text entfernen
        start_tag = '<div style="color: #000000; font-family: Calibri, sans-serif; font-size: 11pt; text-align: initial;">Viele Grüße</div>'
        end_tag = '</body>'

        if start_tag in content:
            start_index = content.index(start_tag)
            end_index = content.index(end_tag, start_index)
            modified_content = content[:start_index] + content[end_index:]

            # Den modifizierten Inhalt zurückschreiben
            with open(file_path, 'w') as file:
                file.write(modified_content)

            print(f"Datei '{filename}' wurde erfolgreich bearbeitet.")

print("Die Aufgabe wurde abgeschlossen.")