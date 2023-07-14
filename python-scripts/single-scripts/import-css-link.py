import os

# Verzeichnis mit den Dateien
directory = "/Users/sby/Library/CloudStorage/OneDrive-PPIAG/korrespondenzvorlage-crossnative/templates"

# Pfad zur CSS-Datei
css_file = "/style.css"

# Text, der ersetzt werden soll
old_text = '<html stemailreadwriter=true> <body stemailreadwriter=true><div style="color: #000000; font-family: Calibri, sans-serif; font-size: 11pt; text-align: initial;">'

# Text, der ersetzen soll
new_text = '''
            <html stemailreadwriter=true>
            <head>
                <meta charset="UTF-8">

                <!--CSS Styles-->
                <link rel="stylesheet" href="style.css">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Archivo:wght@300;700;900&display=swap" rel="stylesheet">
            </head>

            <body stemailreadwriter=true>'''

# Iteration über alle Dateien im Verzeichnis
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        file_path = os.path.join(directory, filename)

        # Datei öffnen und Inhalt lesen
        with open(file_path, "r") as file:
            content = file.read()

        # Text ersetzen
        updated_content = content.replace(old_text, new_text)

        # CSS-Datei kopieren
        css_file_name = os.path.basename(css_file)
        css_destination = os.path.join(directory, css_file_name)
        if not os.path.exists(css_destination):
            os.system(f"cp {css_file} {css_destination}")

        # Aktualisierten Inhalt in Datei schreiben
        with open(file_path, "w") as file:
            file.write(updated_content)

        print(f"In Datei {filename} ersetzt.")

print("Ersetzung abgeschlossen.")
