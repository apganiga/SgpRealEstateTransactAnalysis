@echo off
echo "Start ETLing For RealEstate Data"

set processDate=%date:~10,4%%date:~4,2%%date:~7,2%
set ReportPath=I:\REAL_ESTATE_DATA\REPORTS
set ScriptsPath=G:\MyPyUtils
set recipients=ananth.ganiga@gmail.com,lata.suresh.2014@gmail.com

echo "-- Clearing all HTML and CSV file from Reports Folder"
del /f /q %ReportPath%\*.csv
del /f /q %ReportPath%\*.html

echo "--- Scraping PropGuru Pages"
python G:\WEBSCRAP\REAL_ESTATE\PYSCRIPTS\ScrapePropertyGuruPages.py
echo "--- Pulling PropGuruAds"
python G:\WEBSCRAP\REAL_ESTATE\PYSCRIPTS\PropGuruHTMLpages2Csv.py
echo "--- Pulling SRXProperyAds"
python G:\WEBSCRAP\REAL_ESTATE\PYSCRIPTS\SRXProperyAds.py
echo "--- AuditTableUploader"
start G:\WEBSCRAP\REAL_ESTATE\AuditTableUploader.bat
echo "--- Calling LoadData2_UnitsInMarket_Table"
start G:\WEBSCRAP\REAL_ESTATE\LoadData2_UnitsInMarket_Table.bat
echo "--- Calling Report Generator"
start G:\WEBSCRAP\REAL_ESTATE\Rpt_DiscountedUnitsExtract.bat
echo "--- Moving the report to Today's date..."

move %ReportPath%\DISCOUNTED_BIG_UNITS.csv %ReportPath%\DISCOUNTED_BIG_UNITS_%processDate%.csv
move %ReportPath%\UNITS_DISCOUNTED_PSF_IN_A_CONDO.csv %ReportPath%\UNITS_DISCOUNTED_PSF_IN_A_CONDO_%processDate%.csv

echo "---convert DISCOUNTED_BIG_UNITS csv to HTML"
python %ScriptsPath%\CsvToHtml.py %ReportPath%\DISCOUNTED_BIG_UNITS_%processDate%.csv %ReportPath%\DISCOUNTED_BIG_UNITS_%processDate%.html

echo "---convert UNITS_DISCOUNTED_PSF_IN_A_CONDO csv to HTML"
python %ScriptsPath%\CsvToHtml.py %ReportPath%\UNITS_DISCOUNTED_PSF_IN_A_CONDO_%processDate%.csv %ReportPath%\UNITS_DISCOUNTED_PSF_IN_A_CONDO_%processDate%.html

echo "--Changing Directory to GmailSender"
cd %ScriptsPath%\GmailSender\
echo "---Sending Mail"
set subject=Big_discounted_units_in_market
python SendMail.py %recipients% %subject% %ReportPath%\DISCOUNTED_BIG_UNITS_%processDate%.html --attach %ReportPath%\DISCOUNTED_BIG_UNITS_%processDate%.csv
set subject=Discounted_Units_Based_On_PSF_Comparision
python SendMail.py %recipients% %subject% %ReportPath%\UNITS_DISCOUNTED_PSF_IN_A_CONDO_%processDate%.html --attach %ReportPath%\UNITS_DISCOUNTED_PSF_IN_A_CONDO_%processDate%.csv
move %ReportPath%\DISCOUNTED_BIG_UNITS_%processDate%.* %ReportPath%\ARCHIVE\
