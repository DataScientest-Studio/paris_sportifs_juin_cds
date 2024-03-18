#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date:  16/03/2024

@author: Lionel, Nicolas, Sebastione et François
"""

# Core Pkg
import streamlit as st

# Custom modules

import pandas as pd
from PIL import Image
import numpy as np

# Load the original image
original_image = Image.open("logo_datascientest.png")

# Create a white background image with the same size as the original image
background = Image.new("RGBA", original_image.size, (255, 255, 255, 255))

# Composite the original image on top of the white background
composite_image = Image.alpha_composite(background.convert("RGBA"), original_image.convert("RGBA"))

# Save the composite image with a white background
composite_image.save("logo_datascientest_with_white_bg.png")

# Function to display the home page
def display_home():
    st.write("Welcome to the Home page!")
    # Add an image to the main page
    st.image("ballon.png")

# Function to display the Les Données page
def display_les_donnees():
    st.write("Les Données page.")

# Function to display the Modélisation page
def display_modelisation():
    st.write("Modélisation page.")

# Function to display the Prédiction page
def display_prediction():
    st.write("Les Prédictions page.")

# Function to display the Equipe Projet page
def display_equipe_projet():
    st.write("Equipe Projet:  Lionel, Nicolas, Sebastion et François")

# Set page title
st.title("Les paris sportifs, prédiction des résultats des matchs de football")

# Create a menu in the sidebar
menu = ["Home", "Les Données", "Modélisation", "Prédiction", "Equipe Projet"]
choice = st.sidebar.selectbox("Menu", menu)

# Display content based on menu choice
if choice == "Home":
    display_home()
elif choice == "Les Données":
    display_les_donnees()
elif choice == "Modélisation":
    display_modelisation()
elif choice == "Prédiction":
    display_prediction()
else:
    display_equipe_projet()

# Add some widgets to the main page
st.header("Streamlit Basics")
st.markdown("### Markdown Example")
st.text("This is a text widget")

# Balloons and progress bar
st.balloons()
st.progress(50)

# Temporary waiting message
with st.spinner("Loading..."):
    st.write("This is a temporary waiting message")

# Add an image to the sidebar
st.sidebar.image("dst-logo.svg", width=50)

# Footer
st.markdown("© 2024 DataSciencetest App: Pari Sportif Ligue1")
