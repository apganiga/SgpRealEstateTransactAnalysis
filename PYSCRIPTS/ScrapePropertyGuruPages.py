import pyautogui as gui
import time
import webbrowser
import random
import os
import glob
import shutil

gui.FAILSAFE = False
interval = 2
CLOSE_BROWSER_POS=589,19
PREVIOUS_BROWSER_CLOSE=288,22

URLs = [('PG','https://www.propertyguru.com.sg/property-for-sale/{X}?property_type=N&property_type_code%5B0%5D=APT&property_type_code%5B1%5D=CLUS&property_type_code%5B2%5D=CONDO&property_type_code%5B3%5D=EXCON&property_type_code%5B4%5D=WALK', 10),
       ('AUC', 'https://www.propertyguru.com.sg/property-for-sale/{X}?freetext=Bank+Auction&property_type=N&property_type_code%5B0%5D=APT&property_type_code%5B1%5D=CLUS&property_type_code%5B2%5D=CONDO&property_type_code%5B3%5D=EXCON&property_type_code%5B4%5D=WALK',10),
       ('PFS', 'https://www.propertyguru.com.sg/property-for-sale/{X}?freetext=fire+sale&property_type=N&property_type_code%5B0%5D=APT&property_type_code%5B1%5D=CLUS&property_type_code%5B2%5D=CONDO&property_type_code%5B3%5D=EXCON&property_type_code%5B4%5D=WALK',5)]
#PG = Prop Guru Normal sale
#AUC = Auction sale
#PFS + Prop Guru Fire Sale

tempSaveLocation="C:\\Users\\User\\Downloads"
fileName = '*.html'

for url in URLs[:]:

    oldFilesList = glob.glob(tempSaveLocation + "\\" + fileName)
    for file in oldFilesList:
        print("Removing File:", file)
        os.remove(file)

    scrapeType, urlTemplate, noOfPageReqd = url
    counter= 1
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
        if i > 1:
            print("i={}; closing the browser".format(i))
            gui.click(CLOSE_BROWSER_POS)
            time.sleep(2)
            gui.click(CLOSE_BROWSER_POS)
            time.sleep(2)

    gui.click(CLOSE_BROWSER_POS)
    gui.click(CLOSE_BROWSER_POS)
    finalDest = "I:\\REAL_ESTATE_DATA\\AUTO_GUI_STAGING"
    FilesList = glob.glob(tempSaveLocation + "\\" + fileName )
    for i, file in enumerate(FilesList):
        print("Moving File From:{} | To:{}".format(file, finalDest))
        destFileName = tempSaveLocation + "\\" + scrapeType + '_' + str(i) + '.html'
        print("destFileName=", destFileName)
        print("file=", file)
        shutil.move(file, destFileName )
        print("finalDest=", finalDest)
        shutil.move(destFileName, finalDest)
