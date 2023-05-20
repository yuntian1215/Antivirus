import streamlit as st
from white_list import API
import pandas as pd
import numpy as np




st.sidebar.write('配置')


st.button("启动扫描", on_click=API.scan)
dic = {'白名单文件路径': API.white_list}
df = pd.DataFrame(dic)
st.dataframe(df, width=700)  # Same as st.write(df)

Dir_added = st.text_input(label='添加路径')
st.button("添加路径", on_click=API.add_Dir, args=[Dir_added])
Dir_deleted = st.selectbox("删除路径", options=API.white_list)
st.button("删除路径", on_click=API.del_Dir, args=[Dir_deleted])
