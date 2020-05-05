set DataToolPath="C:\Program Files (x86)\Microsoft SQL Server\150\DTS\Binn"
set PackagePath="G:\WEBSCRAP\REAL_ESTATE\VisualStudio\RE_UnitInMarket_DataUploader\RE_UnitInMarket_DataUploader"
set LogPath="I:\REAL_ESTATE_DATA\PROCESS_LOG"
set processDate=%date:~10,4%%date:~4,2%%date:~7,2%

%DataToolPath%\DTExec.exe /F %PackagePath%\FileProcessingOverLooker.dtsx >> %LogPath%\UnitsInMarketProcessed_%processDate%.log