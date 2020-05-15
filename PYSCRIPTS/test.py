from selenium import webdriver
chrome_path = r"G:\WEBSCRAP\chromedriver_win32\chromedriver.exe"
URL='https://www.propertyguru.com.sg/property-for-sale/4?property_type=N&property_type_code%5B0%5D=APT&property_type_code%5B1%5D=CLUS&property_type_code%5B2%5D=CONDO&property_type_code%5B3%5D=EXCON&property_type_code%5B4%5D=WALK'
driver = webdriver.Chrome(chrome_path)
print(dir(driver.get(URL)))
