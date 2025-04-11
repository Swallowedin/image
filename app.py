import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🎁 Générateur de figurine RGPD")
st.write("Décris ta figurine style cartoon et génère-la avec DALL·E 3 !")

prompt = st.text_area("🧠 Ton prompt", 
    "A cartoon-style collectible toy figure in packaging, retro toy style, violet background, accessories like glasses and a clipboard"
)

if st.button("🎨 Générer l'image"):
    with st.spinner("Création de l'image en cours..."):
        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                n=1,
                size="1024x1024"
            )
            image_url = response.data[0].url
            image = Image.open(BytesIO(requests.get(image_url).content))
            st.image(image, caption="Voici ta figurine RGPD !", use_column_width=True)
        except Exception as e:
            st.error(f"Erreur : {e}")
