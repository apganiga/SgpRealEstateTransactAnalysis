Write-Output "Start ETLing For RealEstate Data"
$processDate=get-date -Format 'yyyyMMdd'
$ReportPath='I:\REAL_ESTATE_DATA\REPORTS'
$ScriptsPath='G:\MyPyUtils'
$recipients='ananth.ganiga@gmail.com,lata.suresh.2014@gmail.com'

function Process-Report { 
  param( $ReportName )
  $processDate=get-date -Format 'yyyyMMdd'
  $DatedReportName = $ReportName.replace('.csv', '_' + $processDate + '.csv')
  $HTMLReportName = $DatedReportName.replace('.csv', '.html')
  $ReportKey=$ReportName.replace('.csv','')
  $ReportSubject = @{ DISCOUNTED_BIG_UNITS = 'Big_discounted_units_in_market' ; 
                    UNITS_DISCOUNTED_PSF_IN_A_CONDO = 'Discounted_Units_Based_On_PSF_Comparision'
               }
  $subject=$ReportSubject[$ReportKey]

  if ( Test-Path $ReportPath\$ReportName )
  {
     move $ReportPath\$ReportName $ReportPath\$DatedReportName
     Write-Output "---convert $ReportName to HTML"
     python $ScriptsPath\CsvToHtml.py $ReportPath\$DatedReportName $ReportPath\$HTMLReportName
     $subject='Big_discounted_units_in_market'
     cd $ScriptsPath\
     python SendMail.py $recipients $subject $ReportPath\DISCOUNTED_BIG_UNITS_$processDate.html --attach $ReportPath\DISCOUNTED_BIG_UNITS_$processDate.csv
     move-item $ReportPath\DISCOUNTED_BIG_UNITS_$processDate.* $ReportPath\ARCHIVE\
   }
}

Write-Output "-- Clearing all HTML and CSV file from Reports Folder"
#Remove-Item -Path C:\Users\User\Downloads\*.html -Force
#Remove-Item -Path $ReportPath\*.csv -Force
#Remove-Item -Path $ReportPath\*.html -Force

Write-Output "--- Scraping PropGuru Pages"
#python G:\WEBSCRAP\REAL_ESTATE\PYSCRIPTS\ScrapePropertyGuruPages.py

Write-Output "--- Pulling PropGuruAds"
#python G:\WEBSCRAP\REAL_ESTATE\PYSCRIPTS\PropGuruHTMLpages2Csv.py

Write-Output "--- Pulling SRXProperyAds"
#python G:\WEBSCRAP\REAL_ESTATE\PYSCRIPTS\SRXProperyAds.py

Write-Output "--- AuditTableUploader"
#start G:\WEBSCRAP\REAL_ESTATE\AuditTableUploader.bat

Write-Output "--- Calling LoadData2_UnitsInMarket_Table"
#start G:\WEBSCRAP\REAL_ESTATE\LoadData2_UnitsInMarket_Table.bat

Write-Output "--- Calling Report Generator"
#start G:\WEBSCRAP\REAL_ESTATE\Rpt_DiscountedUnitsExtract.bat

Write-Output "--- Moving the report to Today's date..."

Process-Report DISCOUNTED_BIG_UNITS.csv
Process-Report UNITS_DISCOUNTED_PSF_IN_A_CONDO.csv
