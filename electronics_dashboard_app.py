# electronics/electronics_dashboard_app.py

import streamlit as st
from PIL import Image
import os

# Set up page config
st.set_page_config(page_title="Electronics Dashboard", layout="centered")

# Title and intro
st.title("🔧 Electronics Circuit Viewer")
st.markdown(
    "Welcome! This dashboard showcases a selection of circuit schematics and PCB layouts I've designed as part of my journey into electronics and embedded systems. "
    "I enjoy building efficient analog and digital systems—from LTspice simulations to real-world PCB prototyping."
)

# Folder where images are stored
image_folder = os.path.dirname(__file__)

# Map circuit names to image filenames and descriptions
circuits = {
    "Barkhausen Oscillator": {
        "file": "Barkhausen.png",
        "desc": "A classic oscillator that uses positive feedback to generate sustained sinusoidal signals. Often studied for its role in feedback theory and oscillation criteria."
    },
    "Differential Amplifier": {
        "file": "DiffAmp.png",
        "desc": "A fundamental analog building block used to amplify the difference between two input voltages. Useful in sensor interfacing and analog signal conditioning."
    },
    "Filter Characterization": {
        "file": "FilterChar.png",
        "desc": "Circuit showing the behavior of filters across frequency to meet DC, AC, and transient gain specs. Great for understanding signal processing fundamentals."
    },
    "Laser Driver Circuit": {
        "file": "LaserDriver.png",
        "desc": "A custom analog design used to drive a laser diode, featuring current limiting and signal modulation. Designed with SPICE simulation in mind."
    },
    "PCB Layout: Security & Accessibility System": {
        "file": "PCB.png",
        "desc": "The custom PCB layout for a smart door lock system that integrates motion detection, keypad input, audio output, and camera modules."
    }
}

# Dropdown selector
selected_name = st.selectbox("Choose a circuit to view:", [""] + list(circuits.keys()))

# If a circuit is selected, show image and description
if selected_name:
    image_path = os.path.join(image_folder, circuits[selected_name]["file"])
    image = Image.open(image_path)
    st.image(image, caption=selected_name, use_container_width=True)
    st.markdown(f"**Description:** {circuits[selected_name]['desc']}")
else:
    st.markdown("---")
    st.info("Use the dropdown above to select and view a circuit.")
