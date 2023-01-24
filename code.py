from pydicom import dcmread
import matplotlib.pyplot as plt
import numpy as np


f=dcmread('D:\\Work\\Insta\\Amanpour.vip\\Image_Processing\\2_ReadingImage\\Image.dcm')


Im=f.pixel_array
plt.imshow(Im,cmap='gray')


f.PatientName ='Patient^One'
f.PatientID = '111111'
f.ContentDate = '20191113'
f.InstitutionName = 'hospital city'
f.Manufacturer = 'GE MEDICAL SYSTEMS'
f.PatientAge = '50'
f.PatientBirthDate = '1972'
f.PatientID = '111111'
f.StationName = 'GEHCGEHC'
f.StudyDate = '20191113'



f.save_as("C:\\Users\\amanp\\Desktop\\Image.dcm")
