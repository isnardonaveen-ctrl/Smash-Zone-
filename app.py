import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Smash Zone Scheduler", page_icon="🎾", layout="centered")

# --- HEADER & LOGO ---
# Ensure "Smash Zone Logo_2.jpg" is in the same folder as this app.py file
st.image("Smash Zone Logo_2.jpg", width=300) 

st.title("Smash Zone Court Scheduler")
st.markdown("Select your location and court below to book your session.")
st.divider()

# --- LOCATIONS & COURTS ---
locations = [
    "Branch 1 - Downtown", 
    "Branch 2 - Westside", 
    "Branch 3 - North Park", 
    "Branch 4 - Eastside", 
    "Branch 5 - South City", 
    "Branch 6 - Central Plaza"
]

selected_location = st.selectbox("Select Branch Location:", locations)

courts = ["Court 1", "Court 2", "Court 3", "Court 4"]
selected_court = st.selectbox("Select Court:", courts)

# --- BOOKING DETAILS ---
date = st.date_input("Select Date:")
time = st.time_input("Select Time:")
name = st.text_input("Full Name:")
email = st.text_input("Email Address:")

if st.button("Book Court"):
    if name and email:
        st.success(f"Success! {selected_court} at {selected_location} has been booked for {name} on {date} at {time}.")
    else:
        st.error("Please enter your name and email to complete the booking.")
