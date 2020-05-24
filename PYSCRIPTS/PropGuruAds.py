import glob
import re
import json
import pandas as pd
from datetime import datetime
import os
import shutil

fileLocation = "I:\\REAL_ESTATE_DATA\\AUTO_GUI_STAGING"
filesToProcess = glob.glob(fileLocation + "\\*.html")
outputDir = "I:\\REAL_ESTATE_DATA\\DATA_TO_PROCESS"
outputFileName = 'UnitsInMarket_'+ datetime.today().strftime('%d_%m_%Y')  + '_PG'+ '.csv'

processedFilesDir = "I:\\REAL_ESTATE_DATA\\AUTO_GUI_STAGING\\PROCESSED_" + datetime.today().strftime('%d_%m_%Y')
if not os.path.exists(processedFilesDir):
    os.makedirs(processedFilesDir)

startPosString = 'listing-card listing-id-'
endPosString = '/shortlist/delete/'

condoDF = pd.DataFrame(columns=['CondoName', 'Price' , 'Area', 'PSF' , 'BedRooms', 'BathRooms', 'Type', 'Tenure', 'TOP', 'AgentName','AgentsNumber', 'PageNo', 'Source', 'AgentsComment','WebSite'])
condoDict = dict()
clearVariable = [None]*10
for file in filesToProcess[:]:
    print("PROCESSING FILE:", file)
    with open(file, encoding="utf8") as fh:
        data = fh.readlines()
    data = ''.join(data)
    skipPos = data.index('"currency":"SGD"}]}') + len('"currency":"SGD"}]}') #Unitl Here was some ads section Hence skipped
    startPos = data.index('{"gaECListings":[', skipPos) # Here will be the Actual begining of Ad Listing
    endPos = data.index('"currency":"SGD"}]}', startPos) + len('"currency":"SGD"}]}') # The last 3 braces }]} is the end of all ad units
    listings = data[startPos: endPos]
    listings = json.loads(listings)
    for listing in listings['gaECListings']:
        listing = listing['productData']
        dataChunkForThisCondo, condoName, price, district, bedrooms, bathrooms, psf,  area, agentName, source = clearVariable
        if 'name' not in listing:
            print("No Condos in this Listing:", listing)
            continue

        listingId = listing['id']
        condoName = listing['name']
        try:
            price = '$'+ str(listing['price']) ## SSIS requirement for Price with $
            district = listing['district'].split('(')
            bedrooms = listing['bedrooms']
            bathrooms = listing['bathrooms']

            startPos = data.index(startPosString + str(listingId))
            endPos = data.index(endPosString + str(listingId))
            dataChunkForThisCondo =  data[startPos:endPos]

            psfPos = dataChunkForThisCondo.index('span>S$&amp;nbsp;')
            psf =  dataChunkForThisCondo[psfPos:psfPos+30]
            psf = psf.replace('span>S$&amp;nbsp;', '').split('&')[0]

            areaPos = dataChunkForThisCondo.index("sqft<")
            area = dataChunkForThisCondo[areaPos-10: areaPos].split('>')[1] + 'sqft'  ## SSIS requirement for Area with sqft

            agentNamePos = dataChunkForThisCondo.index('Listed by <span class="html-tag">&lt;span <span class="html-attribute-name">class</span>="<span class="html-attribute-value">name</span>"&gt;</span>') \
                           + len('Listed by <span class="html-tag">&lt;span <span class="html-attribute-name">class</span>="<span class="html-attribute-value">name</span>"&gt;</span>')
            agentName = dataChunkForThisCondo[agentNamePos:agentNamePos+20].split('<')[0]
            agentName = re.sub("[^a-zA-Z0-9\s]", "", agentName)

            sourcePos = dataChunkForThisCondo.index('class="html-attribute-value html-external-link" target="_blank" href="https://www.propertyguru.com.sg/listing/') + len('class="html-attribute-value html-external-link" target="_blank" href="')
            source = dataChunkForThisCondo[sourcePos:sourcePos+140].split('"')[0]

            agentPos = dataChunkForThisCondo.index('listing-agent-phone-number hide</span>"&gt;</span>') + len('listing-agent-phone-number hide</span>"&gt;</span>')
            agentNumber = dataChunkForThisCondo[agentPos: agentPos+20].split('<')[0].replace(' ','').replace('+65','')


            condoDF = condoDF.append(pd.DataFrame([[condoName, price , area,  psf, bedrooms, bathrooms, 'Condo', '---', '---', agentName, agentNumber, '---', source, '---', 'PG']],
                                                  columns=['CondoName', 'Price' , 'Area', 'PSF' , 'BedRooms', 'BathRooms', 'Type', 'Tenure', 'TOP', 'AgentName','AgentsNumber', 'PageNo', 'Source', 'AgentsComment','WebSite']))
        except ValueError as e:
            print("Error in Listing", listing)
    shutil.move(file, processedFilesDir)

condoDF = condoDF.set_index('CondoName')
print("Writting to ", outputDir , "\\" , outputFileName, "...")
condoDF.to_csv(outputDir + "\\" + outputFileName )

