import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Silent nights in Italy", layout="wide")

# Farben & Styles
st.markdown("""
    <style>
    bsection.main > div {
    background-color: #cceeff;
    }
    .stSlider > div > div > div[role=\"slider\"] {
        background-color: #006400;
    }
    .banner {
        background: linear-gradient(to right, #008000, #ffffff, #ff0000);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 30px;
    }
    .banner h1, .banner h3 {
        margin: 0;
        color: #000;
    }
    .image-placeholder {
        margin-top: 100px;
    }
    </style>
""", unsafe_allow_html=True)

# Layout mit Platzhaltern links und rechts
col1, spacer_left, col2, spacer_right, col3 = st.columns([1, 0.3, 3, 0.3, 1])

# Hilfsfunktion für rotierte Bilder
def rotated_image(img_path, angle):
    st.markdown(f"""
        <div class='image-placeholder' style='transform: rotate({angle}deg); margin-bottom: 40px;'>
            <img src='data:image/png;base64,{image_to_base64(img_path)}' style='width: 100%; border-radius: 10px;'/>
        </div>
    """, unsafe_allow_html=True)

# Base64-Encoder für lokale Bilder
import base64
from pathlib import Path

def image_to_base64(image_path):
    img_bytes = Path(image_path).read_bytes()
    return base64.b64encode(img_bytes).decode()

with col1:
    rotated_image("Wein1.png", -10)
    rotated_image("Wein3.png", 10)

with col2:
    st.markdown("""
        <div class="banner">
            <h1>🍷 Silent nights in Italy 🍷</h1>
            <h3>Willkommen beim besten Guide für unsere Silent-Dinnerparty! Gib einfach deine Werte ein und finde heraus, wie viel Wein du trinken solltest. Wissenschaftlich nicht belegt, aber garantiert richtig!</h3>
        </div>
    """, unsafe_allow_html=True)

    # Eingaben
    height = st.number_input("Körpergröße (cm)", min_value=100, max_value=250, value=170)
    weight = st.number_input("Gewicht (kg)", min_value=30, max_value=200, value=70)
    gender = st.selectbox("Geschlecht", ["weiblich", "männlich"])
    drinking_power = st.slider("Saufstärke (1 = schwach, 10 = Legende)", 1.0, 10.0, 5.5, 0.1)
    swag = st.slider("Swag (1 = uncool, 10 = Ultra Swag)", 1.0, 10.0, 5.5, 0.1)

    if st.button("Weinmenge berechnen"):
        # Referenzwerte
        ref_data = {
            "männlich": {"height": 190, "weight": 80, "base": 1.0},
            "weiblich": {"height": 170, "weight": 60, "base": 0.5}
        }
        ref = ref_data[gender]

        # Einflussgewichte (Swag = 10%, Rest = je 22.5%)
        height_factor = (height / ref["height"]) * 0.225
        weight_factor = (weight / ref["weight"]) * 0.225
        gender_factor = 0.225  # Immer 1 bei passendem Referenzgeschlecht

        # Trinkstärke
        if drinking_power > 5.5:
            drinking_modifier = 1 + (drinking_power - 5.5) * 0.12
        else:
            drinking_modifier = 1 - (5.5 - drinking_power) * 0.12

        # Swag (geringerer Einfluss)
        if swag > 5.5:
            swag_modifier = 1 + (swag - 5.5) * 0.07
        else:
            swag_modifier = 1 - (5.5 - swag) * 0.07

        # Spezialfall: Maximalwerte
        if drinking_power == 10.0 and swag == 10.0:
            st.success("Du solltest ca. 1 million beers trinken 🍻 Mahlzeit")
        else:
            # Berechnung
            base_score = height_factor + weight_factor + gender_factor + 0.225  # +0.225 für drinking_power Basiswert
            wine_amount = ref["base"] * base_score * drinking_modifier * swag_modifier / 0.9  # /0.9 um Swag einzurechnen
            st.success(f"Du solltest ca. {wine_amount:.2f} Liter Wein trinken 🍷 - du geile Sau")

with col3:
    rotated_image("Wein2.png", 10)
    rotated_image("Wein4.png", -10)
