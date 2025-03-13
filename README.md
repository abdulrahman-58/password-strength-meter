# 🔐 Password Strength Meter

## 📌 Overview
This **Password Strength Meter** is a Python-based **Streamlit** app that evaluates a user's password based on security rules. The app provides feedback on password strength and suggests improvements if needed. Additionally, it includes a **password generator** to create strong passwords.

## 🎯 Features
✅ **Password Strength Analysis** (Weak, Moderate, Strong)  
✅ **Feedback & Improvement Suggestions**  
✅ **Blacklist Common Weak Passwords**  
✅ **Generate Strong Passwords**  
✅ **User-Friendly Web Interface using Streamlit**  

## 🛠️ Technologies Used
- **Python** (Regex, String Manipulation, Random Module)
- **Streamlit** (For GUI)

Getting Started
1️⃣ Install UV
First, install UV (if not already installed):

curl -LsSf https://astral.sh/uv/install.sh | sh
For Windows:

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
Verify installation:

uv --version
2️⃣ Create and Initialize the Project
uv init password-strength-meter
cd password-strength-meter
3️⃣ Install Sreamlit (Dependency)
uv add streamlit
4️⃣ Activate UV Virtual Environment (Windows)
.venv\Scripts\activate
For Linux/macOS:

source .venv/bin/activate
5️⃣ Run Password Strength Meter
streamlit run password_strength_meter.py
🎉 That’s it! Your Password Generator is ready to use 🚀

## 🖥️ How It Works
1. Enter a password in the input field.
2. The app evaluates the password based on:
   - Length (Minimum 8 characters)
   - Upper & lowercase letters
   - At least one digit (0-9)
   - At least one special character (!@#$%^&*)
3. Displays password strength (Weak, Moderate, or Strong) with improvement suggestions.
4. Use the **"Generate Strong Password"** button to create a secure password.

## 📌 Example Output
```
🔑 Enter your password: P@ssw0rd
✅ Strong Password!
```
OR
```
🔑 Enter your password: 12345
❌ Weak Password - Improve it using the suggestions below.
❌ Password should be at least 8 characters long.
❌ Include both uppercase and lowercase letters.
❌ Add at least one special character (!@#$%^&*).
```

## 📜 License
This project is open-source and available under the **MIT License**.

---

