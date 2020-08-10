import pyautogui as gui
import time
import webbrowser
import random
import os
import glob
import shutil
import pdb

gui.FAILSAFE = False
interval = 2
CLOSE_BROWSER_POS=589,19
PREVIOUS_BROWSER_CLOSE=288,22

URLs = [('PG','https://www.propertyguru.com.sg/property-for-sale/{X}?property_type=N&property_type_code%5B0%5D=APT&property_type_code%5B1%5D=CLUS&property_type_code%5B2%5D=CONDO&property_type_code%5B3%5D=EXCON&property_type_code%5B4%5D=WALK', 50),
      ('AUC', 'https://www.propertyguru.com.sg/property-for-sale/{X}?freetext=Bank+Auction&property_type=N&property_type_code%5B0%5D=APT&property_type_code%5B1%5D=CLUS&property_type_code%5B2%5D=CONDO&property_type_code%5B3%5D=EXCON&property_type_code%5B4%5D=WALK',50),
       ('PFS', 'https://www.propertyguru.com.sg/property-for-sale/{X}?freetext=fire+sale&property_type=N&property_type_code%5B0%5D=APT&property_type_code%5B1%5D=CLUS&property_type_code%5B2%5D=CONDO&property_type_code%5B3%5D=EXCON&property_type_code%5B4%5D=WALK',50)]
#PG = Prop Guru Normal sale
#AUC = Auction sale
#PFS + Prop Guru Fire Sale

tempSaveLocation="C:\\Users\\User\\Downloads"
fileName = '*.html'
tempFile = 'view-source_*.html'

for url in URLs[:]:

    oldFilesList = glob.glob(tempSaveLocation + "\\" + fileName)
    print("Removing old Files found :", oldFilesList)
    for file in oldFilesList:
        os.remove(file)
    print("===================================================")

    scrapeType, urlTemplate, noOfPageReqd = url
#    counter= 1
    for i in range(1,noOfPageReqd+1):
        url = urlTemplate.replace('{X}', str(i))
        print("url=", url)
        webbrowser.open(url)
        time.sleep(random.randint(6,10))
        gui.hotkey('ctrl', 'u')
        time.sleep(random.randint(5,8))
        gui.hotkey('ctrl', 's')
        time.sleep(2)
        gui.press('enter')
        time.sleep(2)

        justSavedFile = glob.glob(os.path.join(tempSaveLocation, tempFile))[0]
        print("+" * 40)
        print("justSavedFile=", justSavedFile)
        print("moving to", scrapeType + '_' + str(i) + '.html')
        os.rename(justSavedFile, os.path.join(tempSaveLocation, scrapeType + '_' + str(i) + '.html'))
        print("*" * 40)

        if i > 1:
            print("i={}; closing the browser".format(i))
            gui.click(CLOSE_BROWSER_POS)
            time.sleep(2)
            gui.click(CLOSE_BROWSER_POS)
            time.sleep(2)

    gui.click(CLOSE_BROWSER_POS)
    time.sleep(2)
    gui.click(CLOSE_BROWSER_POS)
    time.sleep(2)
    gui.click(CLOSE_BROWSER_POS)


    finalDest = "I:\\REAL_ESTATE_DATA\\AUTO_GUI_STAGING"
    FilesList = glob.glob(os.path.join(tempSaveLocation, "*.html"))
    print(FilesList)
    for i, file in enumerate(FilesList):
        print("Moving File From:{} | To:{}".format(file, finalDest))
        try:
            shutil.move(file, finalDest)
        except Exception as e:
             print(e)
