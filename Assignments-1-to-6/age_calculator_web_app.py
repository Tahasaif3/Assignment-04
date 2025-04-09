# Project 9: Age Calculator 
# Age Calculator Streamlit Web Applidation

import streamlit as st #type:ignore
from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    years_left = 100 - age if age < 100 else 0
    return age, years_left

# Streamlit UI
st.set_page_config(page_title="Age Calculator", page_icon="📅")
st.title("🎂 Age Calculator")

st.markdown("Enter your full date of birth to calculate your exact age and see how many years left until you turn 100.")

# Input fields
day = st.number_input("Day", min_value=1, max_value=31, step=1)
month = st.number_input("Month", min_value=1, max_value=12, step=1)
year = st.number_input("Year", min_value=1900, max_value=date.today().year, step=1)

if st.button("Calculate Age"):
    try:
        birth_date = date(year, month, day)
        age, years_left = calculate_age(birth_date)
        st.success(f"You are {age} years old!")

        if years_left > 0:
            st.info(f"You have {years_left} years left until you turn 100 years old!")
        else:
            st.info("Congratulations! You are 100 years old or older!")
    except ValueError:
        st.error("Invalid date. Please enter a valid birth date.")

# Footer
st.markdown("---")
st.caption("Made by Taha")
