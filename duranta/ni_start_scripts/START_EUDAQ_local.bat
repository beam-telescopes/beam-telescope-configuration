taskkill /f /IM  euLog.exe.exe
taskkill /f /IM  euProd.exe.exe
taskkill /f /IM  euRun.exe.exe
taskkill /f /IM  TestLogCollector.exe.exe
taskkill /f /IM  eulog.exe.exe
taskkill /f /IM  TestDataCollector.exe.exe
taskkill /f /IM  NiProducer.exe.exe
taskkill /f /IM  TLUProducer.exe.exe
taskkill /f /IM  TestRunControl.exe

:: IP of euRun, thus this computer
set HOSTNAME=192.168.22.2

start euRun.exe.exe
timeout /T 3  > nul
start euLog.exe.exe -r tcp://%HOSTNAME%:44000
timeout /T 3  > nul
start TestDataCollector.exe.exe  -r tcp://%HOSTNAME%:44000
timeout /T 3  > nul
start TLUProducer.exe.exe -r tcp://%HOSTNAME%:44000
timeout /T 3  > nul
start NIProducer.exe.exe -r tcp://%HOSTNAME%:44000