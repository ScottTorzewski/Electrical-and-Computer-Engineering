# electronics/electronics_dashboard_app.py

import streamlit as st
from PIL import Image
import os

# Set up page config
st.set_page_config(page_title="Electronics Dashboard", layout="centered")

# Title and description
st.title("🔧 Electronics Circuit Viewer")
st.markdown(
    "Select a circuit or PCB diagram from the dropdown below to view its schematic or layout."
)

# Folder where images are stored
image_folder = os.path.dirname(__file__)
image_files = {
    "Barkhausen Oscillator": "Barkhausen.png",
    "Differential Amplifier": "DiffAmp.png",
    "Filter Characteristics": "FilterChar.png",
    "Laser Driver Circuit": "LaserDriver.png",
    "PCB Layout: Security & Accessibility System": "PCB.png",
}

# Dropdown selector
selected_name = st.selectbox("Choose a circuit to view:", list(image_files.keys()))

# Load and display the selected image
image_path = os.path.join(image_folder, image_files[selected_name])
image = Image.open(image_path)
st.image(image, caption=selected_name, use_container_width=True)
