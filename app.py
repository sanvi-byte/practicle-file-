import streamlit as st
import numpy as np
import pandas as pd

# ====================================================================
# FEATURE 1: DISPLAY THE REQUIRED HEADING
# ====================================================================
st.title("Welcome to AI")
st.subheader("Class 12 Interactive Student Dashboard")
st.write("---")
# ====================================================================
# NEW FEATURE: STUDENT TEXT INPUT & WELCOME MESSAGE
# ====================================================================
st.header("Student Login")

# i. Accept the student's name using a text input box
student_user = st.text_input("Enter your name:")

# ii. Display a welcome message using the entered name (only if the user typed something)
if student_user:
    st.write("Welcome to the AI application,", student_user, "!")
st.write("---")


