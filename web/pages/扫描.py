import streamlit as st
from white_list import API
import numpy as np

Dir_openfile=st.text_input(label='选择扫描路径(若空着即扫描当前路径)')
#st.button("启动扫描", on_click=API.scan, args=[Dir_openfile])
button_clicked = st.button("启动扫描")
if button_clicked:
	on_click=API.scan(Dir_openfile)
	st.write(on_click)
