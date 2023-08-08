import os
import sys

sys.path.insert(0, r'C:\AI\AI_PPROJECT\BUSINESS_LOGIC')
from BUSINESS_LOGIC.UniversalPassport.passport_extractor import PassportDataExtractor
import streamlit as st
from PIL import Image


def load_image(image_file):
    img = Image.open(image_file)
    return img


def mrz_extractor():
    passport_page = st.file_uploader("INPUT PASSPORT FRONT PAGE!!", type=["png", "jpg", "jpeg"])
    if passport_page is not None:
        st.image(load_image(passport_page), width=750)
        temp_dir = "tempDir"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        passport_page_path = os.path.join(temp_dir, passport_page.name)
        with open(passport_page_path, "wb") as f:
            f.write(passport_page.getbuffer())

        mrz_extractor_button = st.sidebar.button("Extract")
        if mrz_extractor_button is not None:
            passportDataExtractor = PassportDataExtractor('config.ini')
            req_id = 'Saksham'
            response = passportDataExtractor.extract_data(passport_page_path, req_id)
            st.json(response)


if __name__ == '__main__':
    mrz_extractor()
