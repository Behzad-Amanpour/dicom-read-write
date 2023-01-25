"""
Inputs:
    You can use "Image.dcm" which I uploaded as a file
"""

# Reading a DICOM file ================================== Behzad Amanpour =======================
from pydicom import dcmread
import matplotlib.pyplot as plt
import numpy as np  # You may or may not need numpy

f = dcmread('An address on you computer or google drive\\Image.dcm')   # This file contains a "header" and an "image" 
Im = f.pixel_array   # Exctracting the image from the file
plt.imshow(Im,cmap='gray')   # Showing the image

# Reading & Changing Header Info ======================== Behzad Amanpour ========================
print (f)

f.PatientName ='Patient^One'
f.PatientID = '111111'
f.ContentDate = '20191113'
f.InstitutionName = 'hospital city'
f.Manufacturer = 'GE MEDICAL SYSTEMS'
f.PatientAge = '50'
f.PatientBirthDate = '1972'
f.PatientID = '111111'
f.StationName = 'GEHCGEHC'
f.StudyDate = '20191113'   # there are much more info in the header

# Writing a new DICOM file ============================== Behzad Amanpour ========================

f.save_as("An address on you computer or google drive\\Image2.dcm")
