import requests
import re

URL = 'https://www.srx.com.sg/search/sale/condo?page=' + str(3)
listings = requests.get(URL)
listings =  listings.text
listings = re.sub('\s+', ' ', listings)
listings = listings.split('<div class="listingContainer">')
print(listings[1])
