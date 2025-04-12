# project_dashboard_app.py

import streamlit as st
from PIL import Image
import os

# Set up page config
st.set_page_config(page_title="Security & Accessibility System Dashboard", layout="centered")

# Title and intro
st.title("🔐 Security & Accessibility System Dashboard")
st.markdown(
    "This interactive dashboard showcases my custom hardware system for secure and accessible user control. "
    "The project integrates mechanical design, PCB layout, and circuit-level understanding to drive Bluetooth-controlled operation using hinged kickbuttons, optical sensors, and embedded electronics."
)

# Folder where images are stored
image_folder = os.path.dirname(__file__)

# Categories of content
section = st.selectbox("Select a section:", ["", "CAD Designs", "PCB Layouts", "Fundamental Circuits"])

# CAD section
if section == "CAD Designs":
    st.header("🛠️ CAD Designs")
    image = Image.open(os.path.join(image_folder, "CAD.png"))
    st.image(image, caption="3D Model of Kickbutton System", use_container_width=True)
    st.markdown(
        "**Description:** A mechanical model showing the hinged kickbutton mechanism used to activate an optical sensor. Designed in Fusion 360, this model demonstrates precise alignment and spatial considerations in electromechanical integration."
    )

# PCB section
elif section == "PCB Layouts":
    st.header("🧩 PCB Layouts")
    image = Image.open(os.path.join(image_folder, "KiCad.png"))
    st.image(image, caption="KiCad Schematic", use_container_width=True)
    st.markdown(
        "**Description:** Circuit schematic designed in KiCad showing the key modules for motion sensing, keypad input, audio output, and camera interface. Also includes electronics switching system for locking mechanism and backup power supply."
    )

    image = Image.open(os.path.join(image_folder, "PCB.png"))
    st.image(image, caption="PCB Layout: Security & Accessibility System", use_container_width=True)
    st.markdown(
        "**Description:** A custom 2-layer PCB that consolidates all critical modules for the security system. Designed for real-world deployment with efficient routing and component placement."
    )

# Fundamental Circuits section
elif section == "Fundamental Circuits":
    st.header("📘 Fundamental Circuits")
    st.markdown(
        "These circuits were built and simulated in LTspice to reinforce low-level intuition. Understanding how signal amplification, filtering, and feedback behave in analog systems is key to designing robust embedded platforms."
    )

    # Individual circuit selection
    fundamental_circuits = {
        "Barkhausen Oscillator": {
            "file": "Barkhausen.png",
            "desc": "Demonstrates sustained sinusoidal output using positive feedback. Key for learning feedback loop stability in analog design."
        },
        "Differential Amplifier": {
            "file": "DiffAmp.png",
            "desc": "Illustrates common-mode rejection and difference amplification. Core to sensor interfacing and analog signal processing."
        },
        "Filter Characterization": {
            "file": "FilterChar.png",
            "desc": "Shows how RC filters shape frequency response, bridging the gap between circuit design and DSP."
        },
        "Laser Driver Circuit": {
            "file": "LaserDriver.png",
            "desc": "Drives a laser diode with controlled current and modulation. Useful for understanding power delivery and protection circuits."
        },
    }

    selected_circuit = st.selectbox("Choose a fundamental circuit to view:", [""] + list(fundamental_circuits.keys()))

    if selected_circuit:
        image_path = os.path.join(image_folder, fundamental_circuits[selected_circuit]["file"])
        image = Image.open(image_path)
        st.image(image, caption=selected_circuit, use_container_width=True)
        st.markdown(f"**Description:** {fundamental_circuits[selected_circuit]['desc']}")
    else:
        st.markdown("---")
        st.info("Select a circuit above to view its schematic and description.")
