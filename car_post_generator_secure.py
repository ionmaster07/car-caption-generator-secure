import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Car Post Generator", layout="centered")
st.title("🚗 Car Post Generator")

# Inputs
name = st.text_input("Car Name")
model = st.text_input("Model")
year = st.text_input("Year")
owner = st.selectbox("Owner Count", ["1st", "2nd", "3rd", "4th+"])
driven = st.text_input("Driven Distance (in KM)")
fuel = st.selectbox("Fuel Type", ["PETROL/HYBRID", "DIESEL/HYBRID", "PETROL", "DIESEL", "PETROL + CNG"])
transmission = st.selectbox("Transmission", ["MANUAL", "AUTOMATIC", "IMT", "CVT", "DSG"])
colour = st.text_input("Colour")
price = st.text_input("Price (in Lakhs)")

if st.button("Generate"):
    fuel = fuel.upper()
    transmission = transmission.upper()

    st.subheader("🟥 YouTube Title")
    st.code(f"{name} | MODEL - {model} | {year} | {owner} OWNER | {driven} KM | {fuel}")

    st.subheader("🟦 YouTube Description")
    st.code(f"""TRANSMISSION - {transmission}
COLOUR - {colour}
PRICE - {price} LAKHS (ON TABLE NEGOTIABLE)
CONTACT - {os.getenv("CONTACT_1")}
""")

    st.subheader("🟧 YouTube Pinned Comment")
    st.code(f"""CONTACT - {os.getenv("CONTACT_1")}
WEBSITE - {os.getenv("WEBSITE")}
INSTAGRAM - {os.getenv("INSTAGRAM")}
FACEBOOK - {os.getenv("FACEBOOK")}
WHATSAPP - {os.getenv("WHATSAPP")}
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
INSURANCE TYPE - COMPREHENSIVE
ASKING PRICE - {price} LAKHS (ON TABLE NEGOTIABLE)
ANY QUERY - {os.getenv("CONTACT_2")}

#carforsale #usedcardelhi #usedcarncr #mahajanmotor #olxautos #verifiedcars #secondhandcars #usedcarsindia #delhicars #cardealerdelhi #budgetcars #cardeals #usedcardealer #preownedcars #olxcars #delhiusedcars #{name.replace(' ', '')} #{model.replace(' ', '')} #{year} #{owner.replace(' ', '')}Owner #{fuel.replace(' ', '')} #{transmission.replace(' ', '')} #{colour.replace(' ', '')}
""")

    st.subheader("🟥 WEBSITE Title")
    st.code(f"{name}")

    st.subheader("🟦 WEBSITE Description")
    st.code(f"{model} | {year} | {owner} OWNER | {driven} KM | {transmission} | {colour}")

    st.subheader("🟪 WhatsApp Title")
    st.code(f"""{name}
YEAR - {year}
MODEL - {model}
DRIVEN - {driven} KM
OWNER - {owner}
FUEL TYPE - {fuel}
COLOUR - {colour}
TRANSMISSION - {transmission}
INSURANCE TYPE - COMPREHENSIVE
""")
