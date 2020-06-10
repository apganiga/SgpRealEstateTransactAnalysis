import requests
import pandas as pd
import re

outputdir = 'I:\\REAL_ESTATE_DATA\\REPORTS'
URL = 'https://condo.singaporeexpats.com/{X}/property/condo'
condoList = dict()
requiredPatterns = ['<div class="title">', '<div>Type:', '<div>Address:', '<div>Developer:', '<div>District:',
                    '<div>Units:', '<div>Tenure:', 'TOP:']

for i in range(2542) :
    url = re.sub('{X}',str(i), URL)
    data = requests.get(url)
    lines = data.text.split('\n')
    try:
        for line in lines:
            for pattern in requiredPatterns :
                if pattern in line :
                    line = re.sub('<.*?>','', line)
                    if not ':' in line:
                        condoName = line.strip()
                        condoList[condoName] = {}
                        print(condoName)
                    else:
                        k, v = line.split(':')
                        condoList[condoName][k] = v
    except Exception as e:
        print("Error Handling page", i)
        print("Error=", e)
        continue
    if i % 100 == 0 :
        outputFile = outputdir + "\\CondoList" + str(i) + '.csv'
        condo_df = pd.DataFrame.from_dict(condoList, orient='index')
        condo_df.info(verbose=True)
        condo_df.to_csv(outputFile)



