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
          
            if API.Infoflag == 2:
                st.info("Please Input a Non-null URL")
            
            elif API.Infoflag == 1:
                message = "<span style='color:green; font-size: 32px;'> Successfully finished! </span> The following are some criteria we provided:"
                st.markdown(message, unsafe_allow_html=True)

                message = f"""<div style='background-color: #f5f5f5; padding: 10px; box-shadow: 2px 2px 5px 0px rgba(0, 0, 0, 0.3);'>
                {API.output_text.get("conclusion")}
                <br><br>
                <ul style='list-style-type: disc; padding-left: 20px;'>
                <li>{API.output_text.get("http")}</li>
                <li>{API.output_text.get("script")}</li>
                </ul></div>"""
                st.markdown(message, unsafe_allow_html=True)
            
            else:
                pass    



                # time.sleep(5)
                # st.experimental_rerun()
             
        else:
            message = "<span style='color:red; font-size: 32px;'> Warning Message! </span> You may solve it by the following infos:"
            st.markdown(message, unsafe_allow_html=True)

            message = """<div style='background-color: #f5f5f5; padding: 10px; box-shadow: 2px 2px 5px 0px rgba(0, 0, 0, 0.3);'>
            This is a warning msg. It means that our crawler meet some problems. You may solve it by the following advice:
            <br><br>
            <ul style='list-style-type: disc; padding-left: 20px;'>
            <li>Maybe the web link you gave is wrong. Please check it again.</li>
            <li>Maybe your network is down. Check your Network.</li>
            <li>May be the dynamic js needs too long to responding, we suggest you crawl the web source page in a virtual environment and send it to the next button.</li>
            </ul></div>"""

            st.markdown(message, unsafe_allow_html=True)

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
       
        st.info("你要更新的关键词有" + update_text)

        update_button_clicked = st.button(label="更新", on_click=API.call_update, args=[update_text])

        if update_button_clicked:
            st.write("Succeesfully update")

        Keywords_deleted = st.selectbox("删除关键词", options=API.keywords_update_list)
        delete_button_clicked = st.button("删除路径", on_click=API.del_Keywords, args=[Keywords_deleted])
        if delete_button_clicked:
            st.write(API.advice_text)

    with file_upload_tab:
        URL_search = st.text_input(label = '输入待检测的URL ~')
        uploaded_file = st.file_uploader("Choose a html file")
        # (filepath, tempfilename) = os.path.split(self.path)
        # (shotname, extension) = os.path.splitext(tempfilename)
        if uploaded_file is not None:
            (shotname, extension) = os.path.splitext(uploaded_file.name) #提取文件名和后缀
            
            if extension == ".html":
                bytes_data = uploaded_file.read()
                html = bytes_data.decode("utf-8")  # 将文件内容转换为字符串
                st.button("开始筛查", on_click=API.call_html_scan, args=[URL_search, html], key=key_value.value())


                if API.Infoflag2 == 0:
                    st.info("Please Input a Non-null URL with a Non-null HTML")
            
                elif API.Infoflag2 == 1:
                    message = "<span style='color:green; font-size: 32px;'> Successfully finished! </span> The following are some criteria we provided:"
                    st.markdown(message, unsafe_allow_html=True)

                    message = f"""<div style='background-color: #f5f5f5; padding: 10px; box-shadow: 2px 2px 5px 0px rgba(0, 0, 0, 0.3);'>
                    {API.output_text2.get("conclusion")}
                    <br><br>
                    <ul style='list-style-type: disc; padding-left: 20px;'>
                    <li>{API.output_text2.get("http")}</li>
                    <li>{API.output_text2.get("script")}</li>
                    </ul></div>"""
                    st.markdown(message, unsafe_allow_html=True)

            else:
                st.info("Please Input a Html File")
            



    with model_update:
        st.write("当前模型版本为：1.0")
        st.button("更新模型", on_click=API.download_model)

global_API.refresh_by_button(page_render)
