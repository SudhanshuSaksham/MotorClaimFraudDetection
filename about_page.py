import streamlit as st


def app():
    st.title("About")
    st.write("""
    Auto insurance fraud includes everything from falsifying facts on insurance applications,
    submitting false reports of stolen vehicles, nonexistent injuries, or damage to fabricating accidents,
    and submitting claim forms for incidents that never occurred.
    
    We use machine learning to predict which claims are likely to be fraudulent. This information can narrow down the
     list of claims that need a further check. It enables an insurer to detect more fraudulent claims.


    """)
