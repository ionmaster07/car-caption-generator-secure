import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Car Post Generator", layout="centered")
st.title("🚗 Car Post Generator")

# Define the contact number here for easy updating
CONTACT_NUMBER = "9810323945"

# Inputs
name = st.text_input("Car Name")
model = st.text_input("Model")
year = st.text_input("Year")
owner = st.selectbox("Owner Count", ["1st", "2nd", "3rd", "4th+"])
driven = st.text_input("Driven Distance (in KM)")

# Fuel Type Selection
fuel = st.selectbox("Fuel Type", ["PETROL/HYBRID", "DIESEL/HYBRID", "PETROL", "DIESEL", "PETROL + CNG", "ELECTRIC"])

transmission = st.selectbox("Transmission", ["MANUAL", "AUTOMATIC", "IMT", "CVT", "DSG"])
colour = st.text_input("Colour")
insurance = st.selectbox("Insurance Type", ["ZERO DEP.", "COMPREHENSIVE", "NO", "THIRD PARTY"])
price = st.text_input("Price (in Lakhs)")

if st.button("Generate"):
    fuel = fuel.upper()
    transmission = transmission.upper()
    insurance = insurance.upper()

    youtube_title = f"{name} | MODEL - {model} | {year} | {owner} OWNER | {driven} KM | {fuel}"
    youtube_desc = f"""TRANSMISSION - {transmission}
COLOUR - {colour}
INSURANCE TYPE - {insurance}
PRICE - {price} LAKHS (ON TABLE NEGOTIABLE)
CONTACT - {CONTACT_NUMBER}"""

    youtube_pinned = f"""WEBSITE - {os.getenv("WEBSITE")}
INSTAGRAM - {os.getenv("INSTAGRAM")}
FACEBOOK - {os.getenv("FACEBOOK")}
WHATSAPP - {os.getenv("WHATSAPP")}"""

    st.subheader("🟥 YouTube Title")
    st.code(youtube_title)

    st.subheader("🟦 YouTube Description")
    st.code(youtube_desc)

    st.subheader("🟥 YouTube Post")
    st.code(f"""{youtube_title}

{youtube_desc}

{youtube_pinned}
""")

    st.subheader("🟨 Hashtags (YouTube)")
    hashtags_static_yt = "#CarForSale,#UsedCarDelhi,#UsedCarNCR,#MahajanMotor,#OLXAutos,#VerifiedCars,#SecondHandCars,#UsedCarsIndia,#DelhiCars,#CarDealerDelhi,#BudgetCars,#CarDeals,#UsedCarDealer,#PreOwnedCars,#OLXCars,#DelhiUsedCars"
    hashtags_dynamic_yt = f"#{name.replace(' ', '')},#{model.replace(' ', '')},#{year},#{owner.replace(' ', '')}Owner,#{fuel.replace(' ', '')},#{transmission.replace(' ', '')},#{colour.replace(' ', '')}"
    full_hashtags_yt = f"{hashtags_static_yt},{hashtags_dynamic_yt}"
    st.code(full_hashtags_yt)

    st.subheader("🟩 Instagram / Facebook Caption")
    
    st.code(f"""{name}
YEAR - {year}
MODEL - {model}
DRIVEN - {driven} KM
OWNER - {owner}
FUEL TYPE - {fuel}
COLOUR - {colour}
TRANSMISSION - {transmission}
INSURANCE TYPE - {insurance}
ASKING PRICE - {price} LAKHS (ON TABLE NEGOTIABLE)
ANY QUERY - {CONTACT_NUMBER}

#carforsale #usedcardelhi #usedcarncr #mahajanmotor #olxautos #verifiedcars #secondhandcars #usedcarsindia #delhicars #cardealerdelhi #budgetcars #cardeals #usedcardealer #preownedcars #olxcars #delhiusedcars #{name.replace(' ', '')} #{model.replace(' ', '')} #{year} #{owner.replace(' ', '')}Owner #{fuel.replace(' ', '')} #{transmission.replace(' ', '')} #{colour.replace(' ', '')}
""")

    st.subheader("🟥 WEBSITE Title")
    # --- UPDATED LINE BELOW ---
    st.code(f"{name} | {fuel}")

    st.subheader("🟦 WEBSITE Description")
    st.code(f"{model} | {year} | {owner} OWNER | {driven} KM | {transmission} | {colour}")

    st.subheader("🟪 WhatsApp Title")
    st.code(f"""YEAR - {year}
MODEL - {model}
DRIVEN - {driven} KM
OWNER - {owner}
FUEL TYPE - {fuel}
COLOUR - {colour}
TRANSMISSION - {transmission}
INSURANCE TYPE - {insurance}
""")
