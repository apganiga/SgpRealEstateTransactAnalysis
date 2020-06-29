import requests
import re
import pandas as pd

alphabets = ['A','B', 'C','D','E','F','G','H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q','R', 'S','T','U','V','X','Y','Z','0-9']
# alphabets = ['A','B']
url_template = 'https://www.srx.com.sg/condo/name/{X}?&maxResults=20&page='
condoList = dict()

for letter in alphabets:
    url_temp = re.sub('{X}', letter, url_template)
    for i in range(1,100):
        url = url_temp + str(i)
        data = requests.get(url)
        data = data.text.split('\n')
        condoName = ""
        for line in data:
            try:
                if '<a class="condo-result-name notranslate" href="/condo' in line:
                    temp = line.split('>')[1]
                    if '(En' in temp:
                        condoName, _, district = temp.split('(')
                    else:
                        condoName, district = temp.split('(')
                    condoName = condoName.strip()
                    district = re.sub('\)','', district)
                    district = district.strip()
                    condoList[condoName] = dict()
                    condoList[condoName]['district'] = district
                    # print("\n")
                    # print("condoName=", condoName, end="")
                elif '<span class="hidden-xs">&#8226;' in line:
                    tenure = line.split(';')[1].split('<')[0]
                    tenure = tenure.strip()
                    # print("|tenure=", tenure, end="")
                    condoList[condoName]['tenure'] = tenure
                elif '<p class="condo-result-addr notranslate">' in line:
                    address = re.sub('</', '', line.split('>')[1])
                    # print("|adress=", address, end="")
                    condoList[condoName]['address'] = address
                elif '<span class="condo-result-top">Built:' in line:
                    if not 'built' in condoList[condoName] :
                        built = line.split(':')[1].split('<')[0]
                        built = built.strip()
                        # print("|built=", built, end="")
                        condoList[condoName]['built'] = built
                else:
                    continue
            except Exception as e:
                print("Error while extracting URL=", url)
                print("CondoName=", condoName)
                continue

        if condoName == "" :
            break

condos_df = pd.DataFrame.from_dict(condoList, orient='index')
print(condos_df)
# condoList.info()
outputFile = 'I:\\REAL_ESTATE_DATA\\REPORTS\\SRX_CondoList.csv'
condos_df.to_csv(outputFile)
