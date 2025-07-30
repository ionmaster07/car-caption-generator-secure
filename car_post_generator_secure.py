import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

st.set_page_config(page_title="Car Post Generator", layout="centered")

st.title("🚗 Car Post Generator")

name = st.text_input("Car Name")
model = st.text_input("Model")
year = st.text_input("Year")
owner = st.selectbox("Owner Count", ["1st", "2nd", "3rd", "4th+"])
driven = st.text_input("Driven Distance (in KM)")

# ✅ UPDATED FUEL TYPE - Only specific options in CAPS
fuel = st.selectbox(
    "Fuel Type",
    ["PETROL/HYBRID", "DIESEL/HYBRID", "PETROL", "DIESEL", "PETROL + CNG"]
)

# ✅ UPDATED TRANSMISSION - All CAPS
transmission = st.selectbox(
    "Transmission",
    ["MANUAL", "AUTOMATIC", "AMT", "CVT", "DSG", "IMT"]
)

colour = st.text_input("Colour")
price = st.text_input("Price (in Lakhs)")

if st.button("Generate"):
    # YouTube Title
    st.subheader("🟥 YouTube Title")
    st.code(f"{name} | MODEL - {model} | {year} | {owner} OWNER | {driven} KM | {fuel}")

    # YouTube Description
    st.subheader("🟦 YouTube Description")
    st.code(f"""TRANSMISSION - {transmission}
COLOUR - {colour}
PRICE - {price} LAKHS (ON TABLE NEGOTIABLE)
CONTACT - {os.getenv("CONTACT_1")}
WEBSITE - {os.getenv("WEBSITE")}
INSTAGRAM - {os.getenv("INSTAGRAM")}
FACEBOOK - {os.getenv("FACEBOOK")}
""")

    # Insta/Facebook Caption
    st.subheader("🟩 Instagram / Facebook Caption")
    st.code(f"""{name}
YEAR - {year}
MODEL - {model}
DRIVEN - {driven} KM
OWNER - {owner}
FUEL TYPE - {fuel}
COLOUR - {colour}
TRANSMISSION - {transmission}
INSURANCE TYPE - COMPREHENSIVE
ASKING PRICE - {price} LAKHS (ON TABLE NEGOTIABLE)
ANY QUERY - {os.getenv("CONTACT_2")}
""")

    # ✅ New WEBSITE Section
    st.subheader("🟨 Website Title")
    st.code(f"{name} | MODEL - {model} | {year} | {owner} OWNER | {driven} KM | {fuel}")

    st.subheader("⬜ Website Description")
    st.code(f"""TRANSMISSION - {transmission}
COLOUR - {colour}""")
