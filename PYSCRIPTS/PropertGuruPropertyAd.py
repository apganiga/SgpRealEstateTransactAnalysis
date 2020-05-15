import requests

URL='https://www.propertyguru.com.sg/property-for-sale/4?property_type=N&property_type_code%5B0%5D=APT&property_type_code%5B1%5D=CLUS&property_type_code%5B2%5D=CONDO&property_type_code%5B3%5D=EXCON&property_type_code%5B4%5D=WALK'
listings = requests.get(URL)
print(listings.reason)