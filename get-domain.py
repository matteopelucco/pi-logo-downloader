import requests
from bs4 import BeautifulSoup
 
def find_domain(company_name):
    # Cerca il dominio ufficiale usando il nome dell'azienda
    # search_url = f"https://www.google.com/search?q={company_name}"
    # search_url = f"https://duckduckgo.com/?q={company_name}"
    search_url = f"https://www.bing.com/search?q={company_name}"

    print(search_url)

    # get Session
    session = requests.Session()

    # and Set Cookie
    cookie = {
        'SOCS': 'CAESHAgBEhJnd3NfMjAyNDA4MDUtMF9SQzEaAmRlIAEaBgiA8sq1Bg'
    }

    # session.cookies.update(cookie)

    response = requests.get(search_url, verify=False)
    print(response.status_code)
    soup = BeautifulSoup(response.content, "html.parser")
 
    # print(soup)

    # Estrai il primo risultato di ricerca (di solito il sito web ufficiale)
    # search_results = soup.find_all("cite", class_="tjvcx GvPZzd dTxz9 cHaqb")
    search_results = soup.find_all("cite")

    

    if search_results:
        domain = search_results[0].text
        return domain
    else:
        return "Dominio non trovato"
 
# Esempio di utilizzo: Trova il dominio per Apple Inc.
company_name = "Apple Inc."
domain = find_domain(company_name)
print(f"Dominio associato a {company_name}: {domain}")