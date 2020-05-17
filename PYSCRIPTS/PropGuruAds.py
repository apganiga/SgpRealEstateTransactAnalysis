import glob
import re
import json
import pandas as pd
from datetime import datetime

fileLocation = "I:\\REAL_ESTATE_DATA\\AUTO_GUI_STAGING"
filesToProcess = glob.glob(fileLocation + "\\*.html")
outputDir = "I:\\REAL_ESTATE_DATA\\UNITS_IN_MARKET"
outputFileName = 'UnitsInMarket_'+ datetime.today().strftime('%d_%m_%Y')  + '_PG'+ '.csv'

condoDF = pd.DataFrame(columns=['CondoName', 'Price', 'BedRooms', 'BathRooms', 'Type', 'Tenure', 'TOP', 'Area', 'PSF', 'AgentsNumber', 'PageNo', 'Source', 'AgentsComment'])
condoDict = dict()
for file in filesToProcess:
    print("PROCESSING FILE:", file)
    with open(file, encoding="utf8") as fh:
        data = fh.readlines()
    data = ''.join(data)
    skipPos = data.index('"currency":"SGD"}]}') + len('"currency":"SGD"}]}')
    startPos = data.index('{"gaECListings":[', skipPos)
    endPos = data.index('"currency":"SGD"}]}', startPos) + len('"currency":"SGD"}]}')
    listings = data[startPos: endPos]
    listings = json.loads(listings)
    for listing in listings['gaECListings']:
        listing = listing['productData']
        if 'name' not in listing:
            print("No Condos in this Listing:", listing)
            continue

        condoName = listing['name']
        try:
            price = listing['price']
            district = listing['district'].split('(')
            bedrooms = listing['bedrooms']
            bathrooms = listing['bathrooms']

            condoForSaleStr = 'title</span>="<span class="html-attribute-value">For Sale - {}</span>'.format(condoName)
            startPos = data.index(condoForSaleStr)

            psfPos = data.index('span>S$&amp;nbsp;',startPos)
            psf =  data[psfPos:psfPos+30]
            psf = psf.replace('span>S$&amp;nbsp;', '').split('&')[0]

            areaPos = data.index("sqft<", startPos)
            area = data[areaPos-10: areaPos].split('>')[1]
            print("area:", area)

            agentPos = data.index('listing-agent-phone-number hide</span>"&gt;</span>', startPos) + len('listing-agent-phone-number hide</span>"&gt;</span>')
            agentNumber = data[agentPos: agentPos+20].split('<')[0].replace(' ','').replace('+65','')

            print("CONDO:", condoName)
            print("PSF:", psf)
            print("agent Number:", agentNumber)
            condoDF = condoDF.append(pd.DataFrame([[condoName, price , area,  psf, bedrooms, bathrooms, 'Condo', '???', '???', agentNumber, '?', 'PG', '---']],
                                                  columns=['CondoName', 'Price' , 'Area', 'PSF', 'BedRooms', 'BathRooms', 'Type', 'Tenure', 'TOP', 'AgentsNumber', 'PageNo', 'Source', 'AgentsComment']))
        except ValueError as e:
            print("Error in Listing", listing)

condoDF = condoDF.set_index('CondoName')
print("Writting to ", outputDir , "\\" , outputFileName, "...")
condoDF.to_csv(outputDir + "\\" + outputFileName )

