import os

signature_file = "/signature-de.html"
directory = "/Users/sby/Library/CloudStorage/OneDrive-PPIAG/korrespondenzvorlage-crossnative/templates"

def insert_signature(file_path):
    with open(file_path, "r") as file:
        html_content = file.read()

    with open(signature_file, "r") as signature:
        signature_html = signature.read()

    # Füge die Signatur ans Ende des HTML-Inhalts hinzu
    modified_html_content = f"{html_content.strip()}\n\n{signature_html}"

    # Speichere den modifizierten HTML-Inhalt zurück in die Datei
    with open(file_path, "w") as file:
        file.write(modified_html_content)

# Durchsuche das Verzeichnis nach HTML-Dateien und füge die Signatur ein
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        file_path = os.path.join(directory, filename)
        insert_signature(file_path)
        print(f"Signatur eingefügt: {filename}")