import requests
import json
import pandas as pd
import yaml
from datetime import datetime

with open('G:\WEBSCRAP\REAL_ESTATE\SgpRealEstateSecrets.yaml','r') as masked_data:
    secrets = yaml.load(masked_data, Loader=yaml.FullLoader)

myAccessKey=secrets['AccessKey']
URL_token = "https://www.ura.gov.sg/uraDataService/insertNewToken.action"
tokenResponse = requests.get(URL_token, headers={'AccessKey':myAccessKey})
mytoken= (tokenResponse.text.split(":"))[3].split('}')[0].replace('"','')

outputDir = 'I:\\REAL_ESTATE_DATA\\URA_TRANSACTIONS'

for i in range(1,5) :
    transactionFileName = 'TransactionData_' + datetime.today().strftime('%d_%m_%Y') + '_' + str(i) + '.csv'
    condoFileName = 'CondoData_' + datetime.today().strftime('%d_%m_%Y') + '_' + str(i) + '.csv'
    df_CondoDetails = pd.DataFrame()
    df_Transactions = pd.DataFrame()
    URL_privateResidenceTransaction = 'https://www.ura.gov.sg/uraDataService/invokeUraDS?service=PMI_Resi_Transaction&batch=' + str(i)
    Response_transaction = requests.get(URL_privateResidenceTransaction, headers={'AccessKey':myAccessKey, 'token':mytoken})
    Response_transaction = Response_transaction.text
    transactions = json.loads(Response_transaction)
    transactions = transactions['Result']

    for transaction_rec in transactions :
        CondoName = transaction_rec['project']
        Street = transaction_rec['street']
        MarketSegment = transaction_rec['marketSegment']
        District = transaction_rec['transaction'][0]['district']
        Tenure = transaction_rec['transaction'][0]['tenure']
        PropertyType = transaction_rec['transaction'][0]['propertyType']
        condoDict = {'CondoName': [CondoName],
                     'Street': [Street],
                     'MarketSegment': [MarketSegment],
                     'District': [District],
                     'PropertyType': [PropertyType]
                    }
        tempdf_CondoDetails = pd.DataFrame.from_dict(condoDict )

        trans = transaction_rec['transaction']
        tempdf_Transactions = pd.DataFrame(trans)
        tempdf_Transactions['CondoName'] = CondoName
        if df_CondoDetails.empty == True:
            df_CondoDetails = tempdf_CondoDetails.copy()
        df_CondoDetails = df_CondoDetails.append(tempdf_CondoDetails)

        if df_Transactions.empty == True:
            df_Transactions = tempdf_Transactions.copy()
        df_Transactions = df_Transactions.append(tempdf_Transactions)

    df_Transactions['contractDate_mm'] = df_Transactions['contractDate'].str[:2]
    df_Transactions['contractDate_yy'] = df_Transactions['contractDate'].str[2:]
    if 'nettPrice' in df_Transactions :
        df_Transactions = df_Transactions.drop(columns=['nettPrice'])
    df_CondoDetails = df_CondoDetails.set_index('CondoName')
    df_Transactions = df_Transactions.set_index('CondoName')

    df_Transactions.to_csv(outputDir + '\\' + transactionFileName )
    df_CondoDetails.to_csv(outputDir + '\\' + condoFileName )