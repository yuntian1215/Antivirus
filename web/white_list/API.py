import streamlit as st
import pandas as pd
import numpy as np
import os
import sys

white_list = ['/home/user1/桌面/Security_Project-main/VirEnv','/img.png']


def add_Dir(dir: str):
    white_list.append(dir)
    print('add_Dir:', white_list)

def del_Dir(dir: str):
    white_list.remove(dir)
    print('del_Dir:', white_list)

def scan():
	a="clamscan"
	#print(len(white_list))
	for i in range(len(white_list)):
		a = a + " " + "--exclude=" + white_list[i]
	#print(a)
	print("开始扫描!\n请稍等...\n")
	d = os.popen(a)
	f = d.read()
	print(f)
	print("扫描完成!\n")
