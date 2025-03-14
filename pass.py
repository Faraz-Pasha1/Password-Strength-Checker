import streamlit as st
import random
import string
import re

# Page Configuration
st.set_page_config(page_title="🔐 Ultimate Password Strength Checker", page_icon="🔑", layout="centered")

# Title & Description
st.title("🔍 Password Strength Checker & Generator")
st.markdown("""
### 🔥 Secure Your Digital World with a Strong Password!
🛡️ Use this **interactive tool** to analyze your password strength and generate a strong one instantly!
🔑 A strong password helps protect your online identity from hackers!
""", unsafe_allow_html=True)

# Function to Generate a Strong Password
def generate_password(length=12):
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+"
    return ''.join(random.choice(all_chars) for _ in range(length))

# Blacklist of Common Passwords
common_passwords = {
    "password", "123456", "qwerty", "abc123", "password123", "admin", "letmein",
    "welcome", "monkey", "football", "iloveyou", "12345678", "sunshine", "123123"
}

# Input Your Password
password = st.text_input("🔑 Enter Your Password", type="password")

# Button to Generate a Strong Password
if st.button("🛠 Generate Strong Password"):
    strong_password = generate_password()
    st.success(f"🔐 Suggested Password: **{strong_password}**")

# Initialize Feedback List & Score
feedback = []
score = 0

# Custom Scoring Weights
weights = {
    "length": 2,
    "uppercase_lowercase": 1,
    "digit": 1,
    "special_char": 1
}

# Strength Bar Colors
strength_colors = ["🔴", "🟠", "🟡", "🟢", "🟣"]

if password:
    # Check if Password is in Blacklist
    if password.lower() in common_passwords:
        feedback.append("❌ This password is **too common** and easily guessed. Please choose another.")
    else:
        # Length Checking
        if len(password) >= 12:
            score += weights["length"]
        elif len(password) >= 8:
            score += 1
        else:
            feedback.append("❌ Password should be **at least 8 characters long.**")

        # Uppercase & Lowercase Checking
        if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
            score += weights["uppercase_lowercase"]
        else:
            feedback.append("🔠 Password should contain **both UPPERCASE and lowercase letters.**")

        # Digit Checking
        if re.search(r'\d', password):
            score += weights["digit"]
        else:
            feedback.append("🔢 Password should contain **at least one digit (0-9).**")

        # Special Character Checking
        if re.search(r'[!@#$%^&*()_+]', password):
            score += weights["special_char"]
        else:
            feedback.append("🔣 Password should contain **at least one special character (!@#$%^&*).**")

    # Determine Strength Level
    strength_levels = {
        0: "❌ **Very Weak!** 🔴",
        1: "⚠️ **Weak!** 🟠",
        2: "🟡 **Moderate!** 🟡",
        3: "🟢 **Strong!** 🟢",
        4: "💪 **Very Strong!** 🟣"
    }
    strength_message = strength_levels.get(min(score, 4), "❓ **Unknown Strength**")

    # Display Strength Message
    st.subheader("🔍 Password Strength Analysis")
    st.markdown(f"### {strength_message}")

    # Display Dynamic Progress Bar
    st.progress(score / 4)

    # Display Feedback
    if feedback:
        st.markdown("## 💡 How to Make Your Password Stronger")
        for tip in feedback:
            st.write(tip)

    # Security Tips
    st.markdown("""
    ---
    🔐 **Pro Security Tips:**  
    ✅ Use a mix of **uppercase, lowercase, numbers, and special characters**  
    ✅ Avoid using **common words or predictable patterns**  
    ✅ Consider using a **passphrase** instead of a single word  
    ✅ Change your passwords **regularly** and avoid reusing them  
    ✅ Use a **password manager** for extra security 🔏  
    """)

else:
    st.info("🔍 **Enter a password above to check its strength!**")
