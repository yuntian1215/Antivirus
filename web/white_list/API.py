#开发者：吴凡
import threading
import streamlit as st
import pandas as pd
import numpy as np
import os
import sys
import time

white_list = [] #white_list数组用于维护白名单
filepath='web/white_list/white_list.txt' #白名单信息存放在该txt文件中，重启后不会丢失
with open(filepath, 'r') as file:
	white_list= file.readlines()

text_output = []
sec=[0,0,0] #sec数组记录三个设置的值

#在白名单数组添加新地址
def add_Dir(dir: str):
	if dir !='' :
		white_list.append(dir)
		with open(filepath, 'a') as file:
			file.write(dir+'\n')
		print('add_Dir:', white_list)
	else:
		st.write('白名单路径不得为空！')

#在原有的白名单数组选择一个地址并删除
def del_Dir(dir: str):
	white_list.remove(dir)
	with open(filepath, 'w') as file:
		for i in range(len(white_list)):
			file.write(white_list[i])
	print('del_Dir:', white_list)

#扫描函数，利用os库中的popen函数执行命令行指令，并用read函数重定向到前端界面。通过sec数组内的值选择是否添加额外的条件
def scan(*args):
	dir = ''.join(args)
	a="clamscan"
	openfile_name = dir
	for i in range(len(white_list)):
		a = a + " " + "--exclude=" + white_list[i]
	if sec[0]==1:
		a = a + " " +"--detect-pua"
	if sec[1]==1:
		a = a + " " +"--max-filesize=20M"
	if sec[2]==1:
		a = a + " " +"--recursive"
	a=a+" "+openfile_name
	#print(a)
	print("开始扫描!\n请稍等...\n")
	d = os.popen(a)
	global f
	f = d.read()
	print(f)
	print("扫描完成!\n")

#扫描线程函数，防止阻塞主进程使网页卡死
def call_scan(dir: str):
	print(dir)
	t = threading.Thread(target=scan, args=dir)
	t.start()
	st.write("开始扫描!  请稍等...")
	t.join()
	text_output.append(f)

