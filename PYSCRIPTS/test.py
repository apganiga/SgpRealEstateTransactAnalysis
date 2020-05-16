from bs4 import BeautifulSoup
import glob
import codecs
import re
import json

fileLocation = "I:\\REAL_ESTATE_DATA\\AUTO_GUI_STAGING"
file = fileLocation + "\\0.html"
# filesToProcess = glob.glob(fileLocation + "\\*.html")
# for file in filesToProcess:
#     print("PROCESSING FILE:", file)
with open(file, encoding="utf8") as fh:
     data = fh.readlines()
data = ''.join(data)
data = str(data.encode("ascii", 'ignore'))
data = data[2:-1]
soup = BeautifulSoup(data, 'html.parser')
soup = str(soup)
skipPos = soup.find('"currency":"SGD"}]}') + len('"currency":"SGD"}]}')
startPos = soup.index('{"gaECListings":[', skipPos)
endPos = soup.index('"currency":"SGD"}]}', startPos) + len('"currency":"SGD"}]}')
listings = soup[startPos: endPos]
listings = json.loads(listings)
print(listings)
#


# print(type(listings))