import streamlit as st

import about_page
import motor_claim_fraud_streamlit
from StreamlitUtils import Utils_streamlit


st.markdown("<h1 style='text-align: center; color: green;'>MOTOR CLAIM FRAUD DETECTION</h1>",
            unsafe_allow_html=True)

app = Utils_streamlit.MultiApp()
app.add_app("Home Page", about_page.app)
app.add_app("Motor Claim Fraud Detection", motor_claim_fraud_streamlit.app)
app.run()
