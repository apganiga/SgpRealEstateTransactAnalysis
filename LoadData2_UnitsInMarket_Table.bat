set DTXE="C:\Program Files (x86)\Microsoft SQL Server\150\DTS\Binn\DTExec.exe"
set Package="G:\WEBSCRAP\REAL_ESTATE\VisualStudio\RE_UnitInMarket_DataUploader\RE_UnitInMarket_DataUploader\Load_UnitsInMarketData_2_Table.dtsx"
set processDate=%date:~10,4%%date:~4,2%%date:~7,2%
set LogPath="I:\REAL_ESTATE_DATA\LOG\SSIS\DATA_LOAD_LOG_%processDate%.log"
%DTXE% /File %Package% > %LogPath%