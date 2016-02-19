taskkill /f /IM  euRun.exe.exe
taskkill /f /IM  euLog.exe.exe
taskkill /f /IM  euProd.exe.exe
taskkill /f /IM  TestLogCollector.exe.exe
taskkill /f /IM  TestDataCollector.exe.exe
taskkill /f /IM  NiProducer.exe.exe
taskkill /f /IM  TLUProducer.exe.exe

set HOSTNAME=192.168.21.2
set COMPUTERNAME=192.168.21.2

start euRun.exe.exe
timeout /T 2  > nul
start TestLogCollector.exe.exe -r tcp://%HOSTNAME%:44000
timeout /T 2  > nul
start TestDataCollector.exe.exe  -r tcp://%HOSTNAME%:44000
timeout /T 2  > nul
start TLUProducer.exe.exe -r tcp://%HOSTNAME%:44000
timeout /T 2  > nul
start NiProducer.exe.exe -r tcp://%HOSTNAME%:44000
