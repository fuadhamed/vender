import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import urllib3

# Desactiva advertencias por desactivar SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

st.title("🛍️ Extracción simple de Vendedores")

def extract_sellers_simple(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, verify=False)
        soup = BeautifulSoup(response.text, "html.parser")
        sellers = soup.find_all("b", {"class": "jsx-2325455629 copy2 primary jsx-3451706699 normal pod-sellerText seller-text-rebrand"})
        return [s.text.strip() for s in sellers]
    except Exception as e:
        st.error(f"Ocurrió un error: {e}")
        return []

url = st.text_input("Ingresa URL de Falabella")
if url:
    data = extract_sellers_simple(url)
    if data:
        df = pd.DataFrame(data, columns=["Vendedor"])
        st.dataframe(df)
    else:
        st.warning("No se encontraron vendedores.")
