import requests
from PIL import Image
from io import BytesIO
import zipfile
import os
 
# Definiamo la tabella con i dati degli stock
stocks = [
    {"NOMEFILE": "US0378331005.png", "ID INTERNO": 765431, "ASSET NAME": "Apple", "ISIN": "US0378331005"},
    {"NOMEFILE": "US1912161007.png", "ID INTERNO": 881723, "ASSET NAME": "Coca Cola", "ISIN": "US1912161007"},
    {"NOMEFILE": "US0378331009.png", "ID INTERNO": 765432, "ASSET NAME": "Nvidia", "ISIN": "US0378731005"},
    {"NOMEFILE": "US1912161004.png", "ID INTERNO": 881721, "ASSET NAME": "Microsoft", "ISIN": "US1982161007"}
]

# Funzione per ottenere il logo
def get_logo_url_clearbit(company_name, size=512):
    # Questa funzione è un esempio e può essere sostituita con una fonte affidabile per ottenere i loghi
    base_url = "https://logo.clearbit.com/"
    domain = f"{company_name.replace(' ', '').lower()}.com"
    return f"{base_url}{domain}?size={size}"

def get_logo_url_logodev(company_name, size=512, token="pk_Pb1dR0GJTiqgDE071csOZw", format="png", greyscale="false"):
    # Questa funzione è un esempio e può essere sostituita con una fonte affidabile per ottenere i loghi
    base_url = "https://img.logo.dev/"
    domain = f"{company_name.replace(' ', '').lower()}.com"
    url = f"{base_url}{domain}?token={token}&size={size}&format={format}&greyscale={greyscale}"
    print(url)
    return url
 
# Funzione per ridimensionare e salvare le immagini
def resize_and_save_image(image_url, file_path, size=(512, 512)):
    response = requests.get(image_url, verify=False)
    image = Image.open(BytesIO(response.content))
    image = image.resize(size)
    image.save(file_path, format="PNG")
 
# Creazione della cartella temporanea per i loghi
os.makedirs('logos', exist_ok=True)
 
# Lista dei file creati
created_files = []
 
# Otteniamo e salviamo i loghi
for stock in stocks:
    logo_url = get_logo_url_logodev(stock["ASSET NAME"])
    file_path = os.path.join('logos', stock["NOMEFILE"])
    resize_and_save_image(logo_url, file_path)
    created_files.append(file_path)
 
# Creazione del file ZIP
zip_filename = 'logos/logos.zip'
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for file in created_files:
        zipf.write(file, os.path.basename(file))
 
# Mostra il file ZIP creato
zip_filename