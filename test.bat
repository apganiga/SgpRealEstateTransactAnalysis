echo "Start ETLing For RealEstate Data"

set processDate=%date:~10,4%%date:~4,2%%date:~7,2%
set ReportPath=I:\REAL_ESTATE_DATA\REPORTS
set ScriptsPath=G:\MyPyUtils

echo "--- Scraping PropGuru Pages"
echo "--- Pulling PropGuruAds"
echo "--- Pulling SRXProperyAds"
echo "--- AuditTableUploader"
echo "--- Calling LoadData2_UnitsInMarket_Table"
echo "--- Calling Report Generator"
echo "--- Moving the report to Today's date..."

echo "---convert to HTML"
echo "--Changing Directory to GmailSender"
cd %ScriptsPath%\GmailSender\
echo "---Sending Mail"
python SendMail.py ananth.ganiga@gmail.com,lata.suresh.2014@gmail.com %ReportPath%\UNITS_BIG_DISCOUNTED_%processDate%.html --attach %ReportPath%\UNITS_BIG_DISCOUNTED_%processDate%.csv
