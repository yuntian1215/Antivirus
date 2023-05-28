#开发者：胡余僮
import streamlit as st
from white_list import API
import numpy as np
import pandas as pd

Dir_openfile=st.text_input(label='选择扫描路径(若空着即扫描当前路径)')
#st.button("启动扫描", on_click=API.scan, args=[Dir_openfile])
button_clicked = st.button("启动扫描")
with st.container():
	output = {'输出消息': API.text_output}
	output_df = pd.DataFrame(output)
	st.dataframe(output_df, width=700)

if button_clicked:
	on_click=API.call_scan(Dir_openfile)
	#st.write(on_click)

#check1-3为三个设置选择框，并维护API.py中的sec数组
check1 = st.checkbox("扫描潜在不受欢迎程序(PUA)", value=False)
if check1:
	API.sec[0]=1
else:
	API.sec[0]=0
check2= st.checkbox("扫描超过20M的文件", value=False)
if check2:
	API.sec[1]=1
else:
	API.sec[1]=0
check3 = st.checkbox("递归扫描文件夹", value=False)
if check3:
	API.sec[2]=1
else:
	API.sec[2]=0

