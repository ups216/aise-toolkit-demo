import streamlit as st
from aise_toolkit_demo.app import app_utiles
import aise_toolkit_demo.utils as utils

st.write(f"Hello world {utils.calculate()}")
st.write(f"Hello world {utils.get_message()}")
st.write(f"Hello world {app_utiles.app_calculate()}")

# show a image from images folder

#st.image(f"{utils.get_temp_folder()}/app/images/diandian.jpg", caption="Diandian")

#st.image("aise_toolkit_demo/app/images/diandian.jpg", caption="Diandian")

st.write(f"Running from PyInstaller bundle: {utils.is_running_in_pyinstaller_bundle()}")
st.write(f"Temp folder: {utils.get_temp_folder()}")
st.write(f"image path: {utils.get_temp_folder()}/app/images/diandian.jpg")