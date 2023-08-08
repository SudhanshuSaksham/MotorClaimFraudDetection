import cv2
import numpy as np
import streamlit as st


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({"title": title, "function": func})

    def run(self):
        st.sidebar.header('Navigation')
        app = st.sidebar.radio('', self.apps, format_func=lambda app: app['title'])
        app['function']()


def get_image(image1_uploader):
    image_bytes = np.asarray(bytearray(image1_uploader.read()), dtype=np.uint8)
    image = cv2.imdecode(image_bytes, 1)
    return image


if __name__ == '__main__':
    pass
