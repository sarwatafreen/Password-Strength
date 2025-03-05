import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Checker", page_icon="🔐", layout="centered")

# Custom CSS for styling
st.markdown("""
<style>
    .main { text-align: center; } 
    .stTextInput { width: 60% !important; margin: auto; }
    .stButton button { width: 50%; background-color: #5E1914; color: yellow; font-size: 18px; }
    .stButton button:hover { background-color: #EFEFE8FF; }
</style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔒 Password Strength Checker")
st.write("Enter your password to check its strength and security level. 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 9:
        score += 1
    else:
        feedback.append("❌ Password must be **at least 9 characters long**.")

    # Upper & Lower case check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    # Numeric check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")

    # Special character check
    if re.search(r"[!@#$%^&*()_+{}\[\]:;'/.,<>?|]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*()_+{}[]:;'/.,<>?|)**.")

    # Display password strength result
    if score == 4:
        st.success("✅ **Strong Password** - Your password is strong and secure.")
    elif score == 3:
        st.info("🔺 **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password** - Your password is weak. Follow the suggestions below to improve its strength.")

    # Show suggestions if needed
    if feedback:
        with st.expander("🔍 **Improve Your Password**"):
            for item in feedback:
                st.write(item)

# Password input field
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong 🔒")

# Button for checking password strength
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("🔴 Please enter a password first!")  # Show warning if password is empty





# import re
# import streamlit as st

# # page styleing
# st.st_page_config(page_title= "Password Checker", page_icon="🔐",
#                   page_icon="🤖",layout="centered")

# # custom css
# st.markdown("""
# <style>
#          .main{ text-align: centre;} 
#             .stTextInput{ width: 60% !important;margin: auto;}
#             .stButton button {width: 50% background-color #5E1914; colour: yellow; font-size: 18px;}
#             .stButton button :hover {background-colour: #EFEFE8FF;}
#             </style>
#             """ ,unsafe_allow_html=True)
# #page title and decription
# st.title("🔒Password Strength Checker")
# st.write("Enter your password to check its strength security level.🔍")

# # function to check passwod strength
# def check_password_strength(password):
#     score = 0
#     feedback = []
#     if len(password)  >= 9:
#         score += 1 #inccrease score by 1
#     else:
#         feedback.append("❌Password must be **atleast 9 characters long**.")

#         if re.search(r"[A-Z]",password and re.search(r"[a-z]",password)):
#             score +=1
#         else:
#             feedback.append(" ❌Password should include** both upper (A-Z)and lower_a-z) case characters letters**.")

#             if re.search(r"\d",password):
#                 score += 1
#             else:
#                 feedback.append("❌ Password should include** at least  one number (0-9)**.")

#                 # special characters
#                 if re.search(r"[ !@#$%^&*()_+[}{:;'/.,<>?|']",password):
#                     score += 1
#                 else:
#                     feedback.append("❌ Incclude **at least one special character (!@#$%^&*()_+[}{:;'/.,<>?|')**.")

#                     # display password strength result
#                     if score == 5:
#                         st.success("✅ ** strong password ** - your password is strong and secure.")
#                     elif score == 4 :
#                         st.info("**🔺🚧Moderate Password** - consider improving security by adding more feature")
#                     else:
#                         st.error("❌ ** Weak Password** - your password is weak Follow the suggestion below to improve it strength it.")
#                         #feedback
#                         if feedback:
#                             with st.expander("🔍** Improve your Password** "):
#                                 for item in feedback:
#                                     st.write(item)
#                                     password = st.text_input("Enter your password",type="password",help="Ensure you password is strong 🔒")

#                                     # Button Worhing
#                                     if st.button("Check strength"):
#                                         if password:
#                                             check_password_strength(password)
#                                         else:
#                                             st.warning("🔴 Please entre a password frist!") # show worning if  password empty