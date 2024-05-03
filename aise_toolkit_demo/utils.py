import sys
import os

def get_message():
    return "utils.py: get_message() called"

def calculate():
    return 42

def is_running_in_pyinstaller_bundle():
    return getattr(sys, 'frozen', False)

def get_temp_folder():
    if getattr(sys, 'frozen', False):
        # we are running in a bundle
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    return bundle_dir