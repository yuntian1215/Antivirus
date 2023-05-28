#开发者：章宇欣，谭昊天
import time
from threading import Thread
import os

scan_output = ''
fresh_output = ''
def call_scan(dir: str):
    t = Thread(target=scan, args=[dir])
    t.start()

def scan(dir: str):
    print(dir)
    f = os.popen("clamscan "+str(dir))
    global scan_output
    scan_output = f.read()

# 模拟扫描
def simu_scan(dir: str):
    print(dir)
    time.sleep(9)
    global scan_output
    scan_output = 'scan_finished!'

    
def call_fresh():
    t = Thread(target=fresh)
    t.start()

def fresh():
    f = os.popen("freshclam")
    global fresh_output
    fresh_output = f.read()

