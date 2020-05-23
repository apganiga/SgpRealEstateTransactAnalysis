import requests
import io
import re
import pandas as pd
import sys
from datetime import datetime

PropAdDf = pd.DataFrame(columns=['CondoName', 'Price' , 'Area', 'PSF' , 'BedRooms', 'BathRooms', 'Type', 'Tenure', 'TOP', 'AgentName','AgentsNumber', 'PageNo', 'Source', 'AgentsComment','WebSite'])
outputDir = "I:\\REAL_ESTATE_DATA\\DATA_TO_PROCESS"
# outputFileName = 'UnitsInMarket_'+ datetime.today().strftime('%d_%m_%Y')  + '.xlsx'
outputFileName = 'UnitsInMarket_'+ datetime.today().strftime('%d_%m_%Y')  + '_SRX' + '.csv'

def extract(pattern, listing, type='str', imp='N', unwanted=[], splitter=[]):
    m = re.search(pattern, listing)
    if m:
        try:
            result = m.group(1).strip()
            if len(unwanted) > 0:
                for chars in unwanted :
                    result = result.replace(chars, "")

            if len(splitter) > 0:
                splitresult = result.split(splitter[0])
                if splitter[1] == len(splitresult):
                    result = splitresult
                elif splitter[1] < len(splitresult):
                    result = splitresult[:splitter[1]+1]
                elif splitter[1] > len(splitresult):
                    # print("expected value=", splitter[1], "But len(splitterResult)=",len(splitresult),"SplitterResult=", splitresult)
                    splitresult.extend(['-']*(splitter[1]-(len(splitresult))))
                    result = splitresult
                    #Apending '-' to remaining expected value
        except Exception as e:
            print("Error:", e)
            if len(splitter) > 0:
                print(splitresult)
                print("Result Returned:", result)
            print("Error While Extracting: pattern")
            print(m)
    else:
        if imp == 'Y':
            result = None
        else:
            if type== 'str':
                result = '---'
            elif type == 'int':
                result = 0
    return result


for i in range(1,21) :
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
    listings = listings.split('<div class="listingContainer ')

    if len(listings) < 2 :
        print("No more listing pages than page-", i)
        break

    listings = listings[1:]
    for listing in listings[:] :
        condoName = extract('<span class="notranslate">(.*?)</span>', listing, type='str', imp='Y', )
        price = extract('<div class="listingDetailPrice">(.*?)</div>', listing, type='int', imp='Y')
        price = price.split('<')[0] ## Requirement for SSIS pockage to prefix $ for Price
        (area, psf) = extract('<div class="listingDetailValues">(.*?)</div>', listing,type='str',imp='N', unwanted=[' ', '(Built)'], splitter=['/',2])
        type = 'Condo'
        (_,tenure, top) = extract('<div class="listingDetailType">(.*?)</div>', listing, type='str', imp='N', unwanted=['<span>', '</span>',' ', '&#8226', 'Condo' ], splitter=[';',3])
        top = top.split('<')[0]

        bedrooms = extract('<div class="listingDetailRoomNo">(.*?)</div>', listing, type='int', imp='N')
        bathrooms = extract('<div class="listingDetailToiletNo">(.*?)</div>', listing, type='int', imp='N')

        agentsName = extract('<a href="/.*?" class="notranslate listingDetailAgentName">(.*?)</a>', listing, type='int', imp='N')
        agentsName = re.sub("[^a-zA-Z0-9\s]","",agentsName)

        agentsNumber = extract('<input class="mobile-number-full" hidden="" value="(\d+)" ?/>', listing, type='str', imp='N')
        agentsComment = extract('<div class="listingDetailAgentAgencyText ">(.*?)</div>', listing,  type='str', imp='N')
        agentsComment = re.sub("[^a-zA-Z0-9\s]","",agentsComment)

        source = extract('<a href="(.*?)" class="listingDetailTitle', listing,  type='str', imp='N', splitter=['"',0])[0]
        # if 'Marina One Residences' in condoName and '710' in area:
        #     print(condoName, source)
        #     print('<a href="(.*?)" class="listingDetailTitle " target= _blank>')
        #     print('-'*30)
        #     print(listing)
        #     exit()
        source = 'https://www.srx.com.sg' + source
        #'                                                                                                                                                                                                                      'Source', 'AgentsComment'
        dictionary = { 'CondoName': [condoName], 'Price': [price] , 'Area':[area], 'PSF': [psf], 'BedRooms': [bedrooms], 'BathRooms': bathrooms,  'Type': [type], 'Tenure': [tenure], 'TOP':[top] , 'AgentName': [agentsName], 'AgentsNumber': [agentsNumber], 'PageNo': [i], 'Source': [source], 'AgentsComment': [agentsComment], 'WebSite':['SRX'] }
        temp_df = pd.DataFrame.from_dict(dictionary)
        PropAdDf = PropAdDf.append(temp_df)
# exit()
PropAdDf = PropAdDf.set_index('CondoName')
# PropAdDf.to_excel(outputDir + '\\' + outputFileName )
print("Writting to ", outputDir , "\\" , outputFileName, "...")
PropAdDf.to_csv(outputDir + "\\" + outputFileName )