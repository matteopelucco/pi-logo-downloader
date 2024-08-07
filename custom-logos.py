import os
import zipfile

from PIL import Image, ImageDraw, ImageFont
 
# Definiamo i dettagli degli stock
stocks = [
    {"NOMEFILE": "US0378331005.png", "ID INTERNO": 765431, "ASSET NAME": "Apple", "ISIN": "US0378331005"},
    {"NOMEFILE": "US1912161007.png", "ID INTERNO": 881723, "ASSET NAME": "Coca Cola", "ISIN": "US1912161007"}
]
 
# Funzione per creare un'immagine semplice con il nome dell'azienda
def create_simple_logo(company_name, file_path, size=(512, 512)):

    image = Image.new('RGBA', size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    text_size = draw.textlength(company_name, font=font)
    text_position = ((size[0] - text_size[0]) // 2, (size[1] - text_size[1]) // 2)
    draw.text(text_position, company_name, fill='black', font=font)
    image.save(file_path, format="PNG")
 
# Creazione della cartella temporanea per i loghi

os.makedirs('logos', exist_ok=True)
 
# Lista dei file creati
created_files = []
 
# Creiamo e salviamo i loghi semplici

for stock in stocks:
    file_path = os.path.join('logos', stock["NOMEFILE"])
    create_simple_logo(stock["ASSET NAME"], file_path)
    created_files.append(file_path)
 
# Creazione del file ZIP

zip_filename = 'logos.zip'

with zipfile.ZipFile(zip_filename, 'w') as zipf:

    for file in created_files:

        zipf.write(file, os.path.basename(file))
 
# Mostra il file ZIP creato

zip_filename
