import requests
import json
import pandas as pd
import yaml

with open('G:\WEBSCRAP\REAL_ESTATE\SgpRealEstateSecrets.yaml','r') as masked_data:
    secrets = yaml.load(masked_data, Loader=yaml.FullLoader)

myAccessKey=secrets['AccessKey']
URL_token = "https://www.ura.gov.sg/uraDataService/insertNewToken.action"
tokenResponse = requests.get(URL_token, headers={'AccessKey':myAccessKey})
mytoken= (tokenResponse.text.split(":"))[3].split('}')[0].replace('"','')

URL_privateResidenceTransaction = 'https://www.ura.gov.sg/uraDataService/invokeUraDS?service=PMI_Resi_Transaction&batch=1'
Response_transaction = requests.get(URL_privateResidenceTransaction, headers={'AccessKey':myAccessKey, 'token':mytoken})
Response_transaction = Response_transaction.text

transactions = json.loads(Response_transaction)
transactions = transactions['Result']
# print(transactions[1])
#
df_CondoDetails = pd.DataFrame(['CondoName', 'street', 'project_type', 'marketSegment', 'district' ])
df_Transactions = pd.DataFrame(['CondoName', 'area', 'floorRange', 'typeOfArea', 'price', 'contractDate', 'tenure', 'typeOfSale' ] )

# print(df_CondoDetails)
# print(df_Transactions)

for transaction in transactions[:10] :
    print(type(transaction))
    print(transaction['transaction'])
    print ("+" * 100)
