import os
import re

directory = "/Users/sby/Library/CloudStorage/OneDrive-PPIAG/korrespondenzvorlage-crossnative/templates"

def process_mail(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    # Find the PS text
    ps_text_match = re.search(r'<div style="color: #000000; font-family: Calibri, sans-serif; font-size: 11pt; text-align: initial;">(PS:.*?)</div>', content, re.DOTALL)
    if ps_text_match:
        ps_text = ps_text_match.group(1).strip()

        # Remove the PS text from the original location
        content = re.sub(r'<div style="color: #000000; font-family: Calibri, sans-serif; font-size: 11pt; text-align: initial;">(PS:.*?)</div>', '', content, flags=re.DOTALL)

        # Insert the PS text before the "Viele Grüße" tag with spacing
        content = content.replace(
            '<br><div style="color: #000000; font-family: Calibri, sans-serif; font-size: 11pt; text-align: initial;">Viele Grüße</div>',
            f'<br><br>{ps_text}<br><div style="color: #000000; font-family: Calibri, sans-serif; font-size: 11pt; text-align: initial;">Viele Grüße</div><br>'
        )

    # Write the updated content back to the file
    with open(file_path, "w") as file:
        file.write(content)

# Process each mail file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        file_path = os.path.join(directory, filename)
        process_mail(file_path)