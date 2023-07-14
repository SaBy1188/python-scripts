import os
import re

directory = "/Users/sby/Library/CloudStorage/OneDrive-PPIAG/korrespondenzvorlage-crossnative/templates"
signature_file = "/Users/sby/Library/CloudStorage/OneDrive-PPIAG/korrespondenzvorlage-crossnative/signature-de.html"
css_file = "/Users/sby/Library/CloudStorage/OneDrive-PPIAG/korrespondenzvorlage-crossnative/style.css"

def process_mail(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    ps_text_match = re.search(
        r'<div style="color: #000000; font-family: Calibri, sans-serif; font-size: 11pt; text-align: initial;">(PS:.*?)</div>',
        content, re.DOTALL)
    if ps_text_match:
        ps_text = ps_text_match.group(1).strip()
        content = re.sub(
            r'<div style="color: #000000; font-family: Calibri, sans-serif; font-size: 11pt; text-align: initial;">(PS:.*?)</div>',
            '', content, flags=re.DOTALL)
        content = content.replace(
            '<br><div style="color: #000000; font-family: Calibri, sans-serif; font-size: 11pt; text-align: initial;">Viele Grüße</div>',
            f'<br><br>{ps_text}<br><div style="color: #000000; font-family: Calibri, sans-serif; font-size: 11pt; text-align: initial;">Viele Grüße</div><br>'
        )

    with open(file_path, "w") as file:
        file.write(content)


def delete_signature(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                content = file.read()

            start_tag = '<div style="color: #000000; font-family: Calibri, sans-serif; font-size: 11pt; text-align: initial;">Viele Grüße</div>'
            end_tag = '</body>'

            if start_tag in content:
                start_index = content.index(start_tag)
                end_index = content.index(end_tag, start_index)
                modified_content = content[:start_index] + content[end_index:]

                with open(file_path, 'w') as file:
                    file.write(modified_content)

                print(f"File '{filename}' has been successfully processed.")

    print("Task completed.")


def insert_signature(file_path):
    with open(file_path, "r") as file:
        html_content = file.read()

    with open(signature_file, "r") as signature:
        signature_html = signature.read()

    modified_html_content = f"{html_content.strip()}\n\n{signature_html}"

    with open(file_path, "w") as file:
        file.write(modified_html_content)


def add_signature(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            file_path = os.path.join(directory, filename)
            insert_signature(file_path)

            print(f"Signature added: {filename}")

    print("The signature has been added to all files.")


def insert_css_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    old_text = '<html stemailreadwriter=true> <body stemailreadwriter=true><div style="color: #000000; font-family: Calibri, sans-serif; font-size: 11pt; text-align: initial;">'
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

    updated_content = content.replace(old_text, new_text)

    with open(file_path, "w") as file:
        file.write(updated_content)


def add_css_file(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            file_path = os.path.join(directory, filename)
            insert_css_file(file_path)

            print(f"Replaced in file: {filename}")

    css_file_name = os.path.basename(css_file)
    css_destination = os.path.join(directory, css_file_name)
    if not os.path.exists(css_destination):
        os.system(f"cp {css_file} {css_destination}")

    print("Replacement completed.")


def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            file_path = os.path.join(directory, filename)
            new_filename = os.path.splitext(filename)[0] + "_CX.html"
            new_file_path = os.path.join(directory, new_filename)
            os.rename(file_path, new_file_path)

            print(f"File renamed: {filename} -> {new_filename}")

    print("File names have been renamed accordingly.")


def main():
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            file_path = os.path.join(directory, filename)
            process_mail(file_path)

    delete_signature(directory)
    add_signature(directory)
    add_css_file(directory)
    rename_files(directory)


if __name__ == "__main__":
    main()