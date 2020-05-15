import requests
import io
import re
import pandas as pd
import sys
from datetime import datetime

PropAdDf = pd.DataFrame(columns=['CondoName', 'Price', 'Type', 'Tenure', 'TOP', 'Area', 'PSF', 'AgentsNumber' ])
outputDir = "I:\\REAL_ESTATE_DATA\\UNITS_IN_MARKET"
# outputFileName = 'UnitsInMarket_'+ datetime.today().strftime('%d_%m_%Y')  + '.xlsx'
outputFileName = 'UnitsInMarket_'+ datetime.today().strftime('%d_%m_%Y')  + '.csv'
for i in range(1,1300) :
    print("Scraping Web Page:", i)
    URL = 'https://www.srx.com.sg/search/sale/condo?page=' + str(i)
    try:
        listings = requests.get(URL)
        listings =  listings.text
    except Exception as e:
        print("While Requesting for URL:", URL)
        print("exception occured:", e)
        continue
    listings = re.sub('\s+', ' ', listings)
    listings = listings.split('<div class="listingContainer">')

    if len(listings) < 2 :
        print("No more listing pages than page-", i)
        break

    listings = listings[1:]
    for listing in listings[:] :
        m = re.search('<span class="notranslate">(.*?)</span>.*<div class="listingDetailPrice">(.*?)</div>.*<div class="listingDetailType">(.*?)</div>.*<div class="listingDetailValues">(.*?)</div>.*<input class="mobile-number-full" hidden="" value="(\d+)" ?/>.*<div class="listingDetailAgentAgencyText ">(.*?)</div>', listing)
        try:
            condoName = m.group(1).strip()
        except Exception as e:
            print("Error while getting the condo Name")
            print(e)
            continue
        price = m.group(2).strip()
        price = re.sub('<div.*','', price)
        price = re.sub('View to offer','0', price)
        details = m.group(3).strip()
        details = re.sub('<.*?span>', '', details)
        details = re.sub('&#8226;', '', details)
        details = re.sub('  ', ' ', details)
        try:
           (type, tenure, top, *_) = details.split(' ')
        except Exception as e:
            print(condoName, "|Error while unpacking details-", details)
            print("Exception:", e)
            splitDetails = details.split(' ')
            if len(splitDetails) == 2 and ( splitDetails[0] == 'Condo' and 'Built' in splitDetails[1]) :
                print("Since only 2 items in detail, setting tenure and type to", splitDetails )
                [type, tenure] = splitDetails

        priceDetails = m.group(4).strip()
        try:
            if '/' in priceDetails:
                (area, psf) = priceDetails.split(' / ')
            else:
                area = priceDetails
                psf = '-'
        except Exception as e:
            print(condoName, "|Error while unpacking priceDetails-", priceDetails)
            print(priceDetails.split(' '))

        agentsNumber = m.group(5).strip()
        agentsComment = m.group(6).strip()
        dictionary = { 'CondoName': [condoName], 'Price': [price], 'Type': [type], 'Tenure': [tenure], 'TOP':[top] , 'Area':[area], 'PSF': [psf], 'AgentsNumber': [agentsNumber], 'PageNo': [i], 'Source': ['SRX'], 'AgentsComment': [agentsComment] }
        temp_df = pd.DataFrame.from_dict(dictionary)
        PropAdDf = PropAdDf.append(temp_df)

PropAdDf = PropAdDf.set_index('CondoName')
# PropAdDf.to_excel(outputDir + '\\' + outputFileName )
print("Writting to ", outputDir , "\\" , outputFileName, "...")
PropAdDf.to_csv(outputDir + "\\" + outputFileName )