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
section = st.selectbox("Select a section:", ["", "Control Platform", "PCB Layouts", "Fundamental Circuits"])

# Control Platform section (was CAD Designs)
if section == "Control Platform":
    st.header("🛠️ Control Platform")
    
    image = Image.open(os.path.join(image_folder, "CAD.png"))
    st.image(image, caption="3D Model of Kickbutton System", use_container_width=True)
    st.markdown(
        "**Description:** A mechanical model showing the hinged kickbutton mechanism used to activate an optical sensor. "
        "Designed in Fusion 360, this model demonstrates precise alignment and spatial considerations in electromechanical integration."
    )
    
    image = Image.open(os.path.join(image_folder, "platform.jpg")).rotate(90, expand=True)
    st.image(image, caption="Assembled Control Platform Prototype", use_container_width=True)
    st.markdown(
        "**Description:** Fully assembled prototype showcasing how the entire security and accessibility system is mounted and arranged. "
        "Key design challenges included meeting a strict 0.05mm tolerance to ensure the ridge does not contact the base when the kickbutton is pressed, "
        "ensuring mechanical durability for repeated foot use, and maintaining ergonomic and compact layout for user accessibility."
    )

# PCB Layouts section
elif section == "PCB Layouts":
    st.header("🧩 PCB Layouts")

    image = Image.open(os.path.join(image_folder, "KiCad.png"))
    st.image(image, caption="KiCad Schematic", use_container_width=True)
    st.markdown(
        "**Description:** Circuit schematic designed in KiCad showing the key modules for motion sensing, keypad input, audio output, and camera interface. "
        "Also includes electronics switching system for locking mechanism and backup power supply. "
        "Challenges included integrating camera data with the Raspberry Pi Pico—ultimately resolved by using an Arduino to interface with the camera "
        "and sending data via UART to the Pico, which handles wireless transmission. Design also addressed board overheating, grounding techniques, "
        "audio distortion, and protection circuits using optocouplers and resistive buffering."
    )

    image = Image.open(os.path.join(image_folder, "PCB.png"))
    st.image(image, caption="Final PCB Layout", use_container_width=True)
    st.markdown(
        "**Description:** A custom 2-layer PCB consolidating all subsystems for the security system. The layout is optimized for signal integrity, "
        "trace efficiency, thermal distribution, and compact footprint, enabling full integration into the platform design."
    )

    image = Image.open(os.path.join(image_folder, "proto.jpg"))
    st.image(image, caption="Prototype V0: Breadboard Version", use_container_width=True)
    st.markdown(
        "**Description:** The first working prototype of the system built on a breadboard. Allowed rapid iteration of control logic, power delivery, "
        "and sensor configuration before moving to PCB fabrication."
    )

    image = Image.open(os.path.join(image_folder, "v1a.jpg")).rotate(90, expand=True)
    st.image(image, caption="Prototype V1A: First PCB Version", use_container_width=True)
    st.markdown(
        "**Description:** Initial test PCB version integrating core modules. Served to validate electrical continuity, trace performance, and "
        "real-world sensor behavior under load."
    )

    image = Image.open(os.path.join(image_folder, "v1b.jpg")).rotate(90, expand=True)
    st.image(image, caption="Prototype V1B: PCB with Refined Routing", use_container_width=True)
    st.markdown(
        "**Description:** Iterated Camera module using Pico-Arduino UART connection. Sends image data over wifi to remote device for viewing. Final pre-deployment version before full platform assembly."
    )

# Fundamental Circuits section
elif section == "Fundamental Circuits":
    st.header("📘 Fundamental Circuits")
    st.markdown(
        "These circuits were built and simulated in LTspice to reinforce low-level intuition. Understanding how signal amplification, filtering, and feedback behave in analog systems is key to designing robust embedded platforms."
    )

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
