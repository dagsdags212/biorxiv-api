import requests

BASE_URL = "https://www.biorxiv.org"
url = BASE_URL + "/collection/bioinformatics"

def fetch_html(url: str):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text

