import threading
import streamlit as st
import pandas as pd
import numpy as np
import os
import sys
import time

white_list = ['/VirEnv','/img.png','/global_API.py']
text_output = []

def add_Dir(dir: str):
    white_list.append(dir)
    print('add_Dir:', white_list)

def del_Dir(dir: str):
    white_list.remove(dir)
    print('del_Dir:', white_list)

def scan(*args):
	dir = ''.join(args)
	a="clamscan"
	#openfile_name="/mnt/hgfs/share/Security_Project/web"
	openfile_name = dir
	#print(len(white_list))
	for i in range(len(white_list)):
		a = a + " " + "--exclude=" + white_list[i]
	a=a+" "+openfile_name
	#print(a)
	print("开始扫描!\n请稍等...\n")
	d = os.popen(a)
	f = d.read()
	print(f)
	print("扫描完成!\n")
	text_output.append("扫描完成!")
	return f

# #模拟扫描程序
# def scan(*args):
# 	print(args)
# 	dir = ''.join(args)
# 	print(dir)
# 	time.sleep(10)
# 	text_output.append("扫描完成!")
# 	print("扫描完成")


def call_scan(dir: str):
	print(dir)
	t = threading.Thread(target=scan, args=dir)
	t.start()
	print("开始扫描!  请稍等...")
	text_output.append("开始扫描!  请稍等...")
