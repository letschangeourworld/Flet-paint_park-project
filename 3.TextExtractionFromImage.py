'''
Text Extraction from Images
'''



import flet as ft
from flet import *
import pytesseract      # Ned to install pytesseract
from PIL import Image
import os

# make a virtual environmetn based on python and install pytesseract through pip
# Download pytesseract installation file in this site below :
# https://githu.com/UM-Mannheim/tesseract/wiki
# Select your own language in Additional language/scrip data during installation
# Add the path of pytesseract directory installed into the environment varibale of your pc
# Force to designate the directory of pytesseract excution as follows

