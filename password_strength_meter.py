import streamlit as st
import re
import random
import string

# Common weak passwords blacklist
BLACKLISTED_PASSWORDS = {"password", "123456", "123456789", "qwerty", "abc123", "password1", "12345678"}

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Blacklist check
    if password.lower() in BLACKLISTED_PASSWORDS:
        return 0, ["❌ This password is too common. Choose a unique one!"]
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    return score, feedback

# Function to generate a strong password
def generate_strong_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(12))

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("Enter a password to check its strength.")

password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)
    
    # Strength display
    if score == 5:
        st.success("✅ Strong Password!")
    elif score >= 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below.")
    
    # Show feedback
    for msg in feedback:
        st.write(msg)

# Generate strong password button
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.success(f"🔑 Suggested Strong Password: `{strong_password}`")

