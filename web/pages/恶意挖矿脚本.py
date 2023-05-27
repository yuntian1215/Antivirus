import streamlit as st
from crypto_jacking import API
import pandas as pd
import global_API
import streamlit as st
import pandas as pd
import time
from PIL import Image
import pytesseract

def page_render(key_value):
    function_tab, file_upload_tab, settings_tab,  = st.tabs(["挖矿脚本筛查", "HTML文件上传", "实时更新"])

    with function_tab:
        URL_search = st.text_input(label = '输入待检测的URL 👇')
        print(URL_search)
        st.write("You entered URL is: ", URL_search)
        st.button("开始筛查", on_click=API.call_scan, args=[URL_search])
        
        if API.flag:
            st.dataframe(pd.DataFrame({'输出信息': API.output_text}), width=700)

            # time.sleep(15)
            # st.experimental_rerun()
        
             
        else:
            st.write(API.failure_warning)

    with settings_tab:
        settings_file = st.file_uploader("Choose a img file")
        
        text = "Please input the latest keywords in lines"
        # 利用OCR提取图片文字
        if settings_file is not None:
            image = Image.open(settings_file)
            text = pytesseract.image_to_string(image)
            update_text = st.text_area(label='setting_text', value=text)
        else:
            update_text = st.text_area(label='setting_text', value=text)
       
        st.write("你要更新的关键词有", update_text)
        update_button_clicked = st.button(label="更新", on_click=API.call_update, args=[update_text])
        
        if update_button_clicked:
            st.write(API.advice_text)

    with file_upload_tab:
        URL_search = st.text_input(label = '输入待检测的URL ~')
        uploaded_file = st.file_uploader("Choose a html file")
        
        if uploaded_file is not None:
            bytes_data = uploaded_file.read()
            html = bytes_data.decode("utf-8")  # 将文件内容转换为字符串
            st.button("开始筛查", on_click=API.call_html_scan, args=[URL_search, html], key=key_value.value())

            st.dataframe(pd.DataFrame({'输出信息': API.output_text2}), width=700)


global_API.refresh_by_button(page_render)
