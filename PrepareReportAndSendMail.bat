@echo off
echo "Start ETLing For RealEstate Data"

set processDate=%date:~10,4%%date:~4,2%%date:~7,2%
set ReportPath=I:\REAL_ESTATE_DATA\REPORTS
set ScriptsPath=G:\MyPyUtils

start G:\WEBSCRAP\REAL_ESTATE\LoadData2_UnitsInMarket_Table.bat
echo "--- Calling Report Generator"
start G:\WEBSCRAP\REAL_ESTATE\Rpt_DiscountedUnitsExtract.bat
echo "--- Moving the report to Today's date..."

move %ReportPath%\UNITS_BIG_DISCOUNTED.csv %ReportPath%\UNITS_BIG_DISCOUNTED_%processDate%.csv
echo "---convert to HTML"
python %ScriptsPath%\CsvToHtml.py %ReportPath%\UNITS_BIG_DISCOUNTED_%processDate%.csv %ReportPath%\UNITS_BIG_DISCOUNTED_%processDate%.html
echo "--Changing Directory to GmailSender"
cd %ScriptsPath%\GmailSender\
echo "---Sending Mail"
python SendMail.py ananth.ganiga@gmail.com,lata.suresh.2014@gmail.com %ReportPath%\UNITS_BIG_DISCOUNTED_%processDate%.html --attach %ReportPath%\UNITS_BIG_DISCOUNTED_%processDate%.csv
