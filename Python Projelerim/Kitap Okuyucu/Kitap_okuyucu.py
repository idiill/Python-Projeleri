#pip install pyttsx3 ve pip install PyPDF2 yüklüuoruz

import pyttsx3
import PyPDF2

hikaye=open("fuelcell.pdf","rb")

pdf_okuyucu=PyPDF2.PdfFileReader(hikaye)

engine=pyttsx3.init()
voices=engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)   #kadın sesi [0], erkek sesi [1]

for sayfa_numarası in range(0,pdf_okuyucu.numPages):
    sayfa=pdf_okuyucu.getPage(sayfa_numarası)
    yazi=sayfa.extractText()
    engine.say(yazi)
    engine.runAndWait()