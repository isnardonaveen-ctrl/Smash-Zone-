# app.py
import streamlit as st

# Configure the browser tab
st.set_page_config(page_title="Smash Zone Scheduler", layout="wide")

# --- BRANCH AND COURT DATA ---
BRANCHES = {
    "Smashville": ["Court 1", "Court 2", "Court 3"],
    "Creekside": ["Court 1", "Court 2", "Court 3"],
    "Main Branch": ["Court 1", "Court 2", "Court 3"],
    "Hillside": ["Court 1", "Court 2", "Court 3"],
    "Caibaan": ["Court 1", "Court 2", "Skinny Court"],
    "Downtown": ["Court 1", "Court 2", "Court 3", "Court 4", "Court 5", "Court 6", "Court 7", "Court 8"],
}

HOURS = [
    "08:00 AM", "09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", 
    "01:00 PM", "02:00 PM", "03:00 PM", "04:00 PM", "05:00 PM", 
    "06:00 PM", "07:00 PM"
]

# --- INITIALIZE DATABASE (Mocking a real database using Streamlit State) ---
if "bookings" not in st.session_state:
    st.session_state.bookings = {
        # Pre-filling some mock bookings to show how it works
        "Smashville-Court 1-09:00 AM": {"name": "John Doe", "email": "john@example.com"},
        "Downtown-Court 5-11:00 AM": {"name": "Coach Mike", "email": "mike@example.com"}
    }

# --- HEADER ---
st.title("🏓 SMASH ZONE")
st.markdown("Select your location and court below to book your session.")
st.divider()

# --- PRIMARY NAVIGATION: BRANCH TABS ---
# We use a horizontal radio button list to act as tabs
selected_branch = st.radio("📍 Select Branch", list(BRANCHES.keys()), horizontal=True)

# --- SECONDARY NAVIGATION: COURT TABS ---
courts_in_branch = BRANCHES[selected_branch]
selected_court = st.radio("🎾 Select Court", courts_in_branch, horizontal=True)

st.divider()
st.subheader(f"Availability for {selected_branch} - {selected_court}")

# --- SCHEDULER GRID ---
# We create a 4-column layout for the timeslots
cols = st.columns(4)

for index, time in enumerate(HOURS):
    # Distribute the timeslots evenly across the 4 columns
    col = cols[index % 4]
    
    # Create a unique key for each specific slot
    booking_key = f"{selected_branch}-{selected_court}-{time}"
    is_booked = booking_key in st.session_state.bookings
    
    with col:
        if is_booked:
            # If the slot is taken, display a red error box with the booker's name
            booker_name = st.session_state.bookings[booking_key]["name"]
            st.error(f"**{time}**  \nReserved by {booker_name}")
        else:
            # If the slot is open, create a popover button for the booking form
            with st.popover(f"Book {time}", use_container_width=True):
                st.write(f"**Confirm Booking for {time}**")
                
                # The form the user fills out
                with st.form(key=f"form_{booking_key}"):
                    name = st.text_input("Full Name")
                    email = st.text_input("Email")
                    phone = st.text_input("Phone Number")
                    
                    submit_button = st.form_submit_button("Confirm Booking")
                    
                    if submit_button:
                        if name and email:
                            # Save the booking to our state
                            st.session_state.bookings[booking_key] = {
                                "name": name, 
                                "email": email, 
                                "phone": phone
                            }
                            # Refresh the app to show the new booking
                            st.rerun()
                        else:
                            st.warning("Please fill out your name and email.")
