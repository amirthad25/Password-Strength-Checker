import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Password is too short! Use at least 8 characters.")

    # Check uppercase & lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🟠 Add both uppercase and lowercase letters.")

    # Check numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🟠 Add at least one number.")

    # Check special characters
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback.append("🟠 Add at least one special character (e.g., @, $, !, etc.).")

    # Determine strength level
    if score >= 4:
        strength = "✅ Strong"
        color = "green"
    elif score >= 2:
        strength = "🟡 Medium"
        color = "orange"
    else:
        strength = "🔴 Weak"
        color = "red"

    return strength, color, feedback

# Streamlit UI
st.title("🔑 Password Strength Checker")
st.write("Enter a password below to check its security level.")

# Password input
password = st.text_input("Enter your password", type="password")

if password:
    strength, color, feedback = check_password_strength(password)
    st.markdown(f"### **Password Strength: <span style='color:{color};'>{strength}</span>**", unsafe_allow_html=True)
    
    if feedback:
        st.subheader("💡 Tips to Improve:")
        for tip in feedback:
            st.write(f"- {tip}")
