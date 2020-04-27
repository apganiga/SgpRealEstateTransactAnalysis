import requests
import io
import re
import pandas

URL = 'https://www.srx.com.sg/search/sale/condo?page=2'
listings = requests.get(URL)
listings =  listings.text
listings = re.sub('\s+', ' ', listings)
listings = listings.split('<div class="listingContainer">')
listings = listings[1:]
for listing in listings[:1] :
    print(listing)
    m = re.search('<span class="notranslate">(.*?)</span>.*<div class="listingDetailPrice">(.*?)</div>.*<div class="listingDetailType">(.*?)</div>.*<div class="listingDetailValues">(.*?)</div>', listing)
    # m = re.search('data-premium=(.*)', listing)
    print("----------------------------")
    condoName = m.group(1)
    price = m.group(2)
    details = m.group(3)
    details = re.sub('<.*?span>', '', details)
    details = re.sub('&#8226;', '', details)
    priceDetails = m.group(4)
    print("condoName={}, price={}, details={}, priceDetails={}".format(condoName, price, details, priceDetails))


