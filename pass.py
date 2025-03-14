import streamlit as st
import re


# Page HEading
st.set_page_config(page_title="🔐 Ultimate Password Strength Checker", page_icon="🔑", layout="centered")

# Title and Description of the page or project
st.title("🔍 Password Strength Checker")
st.markdown("""
### 🔥 Secure Your Digital World with a Strong Password!
🛡️ Use this **interactive tool** to analyze your password strength.  
🔑 A strong password helps protect your online identity from hackers!  
""", unsafe_allow_html=True)

# Input Your Password
password = st.text_input("🔑 Enter Your Password", type="password")

# Initialize Feedback List and Score
feedback = []
score = 0

# Strength Bar Colors
strength_colors = ["🔴", "🟠", "🟡", "🟢", "🟣"]

if password:
    # Length Checking
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long.**")

    # Uppercase & Lowercase Checking
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔠 Password should contain **both UPPERCASE and lowercase letters.**")

    # Digit Checking
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔢 Password should contain **at least one digit (0-9).**")

    # Special Character Checking
    if re.search(r'[!@#$%^&*()_+]', password):
        score += 1
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
    strength_message = strength_levels.get(score, "❓ **Unknown Strength**")

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