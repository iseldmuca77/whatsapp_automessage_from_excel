from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import socket
import getpass
import os
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import csv
from tkinter import *
from tkinter import filedialog as fd


mGui = Tk()
mGui.geometry("800x400")
mGui.title('WhatsApp Bot')
mGui.configure(bg='#66CDAA')

Label(mGui,background='#66CDAA', text = "Input time between sent message: ", fg='white', font=('Calibri', 18, 'bold')).pack()
x = Entry(mGui)
x.pack(pady=30)

def getInput():
    a = x.get()

    global params
    params = [a]

y = Button(mGui, text = "Submit",bd = '4', fg='black',font=('Calibri', 14 , 'bold'),command=getInput,)
y.pack(pady=30)

mesazh = Label(
    text = "Input path of excel: ",
    bg = '#66CDAA',
    fg='white', 
    font=('Calibri', 18, 'bold')
)
mesazh.pack(pady=30)

buton = Button(mGui,text="Browse",bd = '4', bg = 'white', fg = 'black',font =('Calibri', 14, 'bold'),command=mGui.destroy)
buton.pack(pady=30)

mGui.mainloop()

numrat_telefonit = fd.askopenfilename()
koha_1 = int(params[0])


data = pd.read_csv(numrat_telefonit)
data_dict = data.to_dict('list')
leads = data_dict['Numri']
messages = data_dict['Mesazhi']
combo = zip(leads,messages)

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("http://web.whatsapp.com")
time.sleep(10)

csvfile = open('numrat qe kane whatsapp.csv', 'w', newline='')

for numra,mesazhe in combo:
    driver.get("https://web.whatsapp.com/send?phone="+str(numra)+"&text="+mesazhe)
    time.sleep(5)
    try:
        #shkruaj = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        time.sleep(koha_1)
    except NoSuchElementException:
        time.sleep(5)