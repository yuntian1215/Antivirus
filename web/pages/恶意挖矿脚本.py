import streamlit as st
from crypto_jacking import API
import global_API
import streamlit as st
import pandas as pd
import time
from PIL import Image
import pytesseract
import os

def page_render(key_value):
    function_tab, file_upload_tab, settings_tab,model_update  = st.tabs(["挖矿脚本筛查", "HTML文件上传", "实时更新","更新模型"])

    with function_tab:
        URL_search = st.text_input(label = "输入待检测的URL 👇")
        st.write("You entered URL is: ", URL_search)
        st.button("开始筛查", on_click=API.call_scan, args=[URL_search])
        
        if API.flag:
            st.dataframe(pd.DataFrame({"输出信息": API.output_text}), width=700)

            if API.Infoflag:
                st.info("Please Input a Non-null URL")

            # time.sleep(5)
            # st.experimental_rerun()
             
        else:
            failure_warning = "This is a warning msg\n It means that our crawler meet some problems\n You may solve it by the following advice:\n First: Maybe your network is down. Check your Internet Links.  Second: May be the dynamic js needs too long to responding, we suggest you crawl the web source page in a virtual environment and send it to the next button\n"

            st.info("failure_warning")

    with settings_tab:
        settings_file = st.file_uploader("Choose a img file")

        text = "Please input the latest keywords in lines"
        # 利用OCR提取图片文字
        if settings_file is not None:
            (shotname, extension) = os.path.splitext(settings_file.name)  # 提取文件名和后缀
            if extension == ".png" or extension == ".jpg":
                image = Image.open(settings_file)
                text = pytesseract.image_to_string(image)
                update_text = st.text_area(label='setting_text', value=text)
            else:
                st.info("上传的文件类型不是图片类型的")
                update_text = st.text_area(label='setting_text', value=text)
        else:
            update_text = st.text_area(label='setting_text', value=text)
       
        st.write("你要更新的关键词有", update_text)

        update_button_clicked = st.button(label="更新", on_click=API.call_update, args=[update_text])
        delete_button_clicked = st.button(label="删除关键字", on_click=API.call_update, args=[update_text])

        if update_button_clicked:
            st.write(API.advice_text)

    with file_upload_tab:
        URL_search = st.text_input(label = '输入待检测的URL ~')
        uploaded_file = st.file_uploader("Choose a html file")
        # (filepath, tempfilename) = os.path.split(self.path)
        # (shotname, extension) = os.path.splitext(tempfilename)
        if uploaded_file is not None:
            (shotname, extension) = os.path.splitext(uploaded_file.name) #提取文件名和后缀
            print(shotname)
            if extension == ".html":
                bytes_data = uploaded_file.read()
                html = bytes_data.decode("utf-8")  # 将文件内容转换为字符串
                st.button("开始筛查", on_click=API.call_html_scan, args=[URL_search, html], key=key_value.value())

                st.dataframe(pd.DataFrame({'输出信息': API.output_text2}), width=700)
            else:
                st.info("上传的文件类型不是HTML类型的")

    with model_update:
        st.write("当前模型版本为：1.0")
        st.button("更新模型", on_click=API.download_model)

global_API.refresh_by_button(page_render)
