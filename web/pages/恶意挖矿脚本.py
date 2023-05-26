import streamlit as st
from crypto_jacking import API
import pandas as pd
from io import StringIO


function_tab, settings_tab, file_upload_tab,  = st.tabs(["挖矿脚本筛查", "实时更新", "HTML文件上传"])
with function_tab:
    URL_search = st.text_input(label='输入URL')
    st.button("开始筛查", on_click=API.call_scan, args=[URL_search])
    if API.flag:
        st.dataframe(pd.DataFrame({'输出信息': API.output_text}), width = 700)
    else:
        st.write(API.failure_warning)

with settings_tab:
    settings_file = st.file_uploader("Choose setting file")
    API.setting_text = st.text_area(label='setting_text', value=API.update_text, on_change=API.change_update_text, args=[API.setting_text])
    update_button_clicked = st.button(label="更新", on_click=API.call_update)
    if update_button_clicked:
        st.write(API.advice_text)

with file_upload_tab:
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # # Can be used wherever a "file-like" object is accepted:
        # dataframe = pd.read_csv(uploaded_file)
        # st.write(dataframe)

