from threading import Thread
import os

scan_output = ''

def call_scan(dir: str):
    t = Thread(target=scan, args=[dir])
    t.start()

def scan(dir: str):
    print(dir)
    f = os.popen("clamscan "+str(dir))
    global scan_output
    scan_output = f.read()
    
def call_fresh():
    t = Thread(target=fresh)
    t.start()

def fresh():
    f = os.popen("freshclam")
