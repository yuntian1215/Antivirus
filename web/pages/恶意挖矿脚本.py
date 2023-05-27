import streamlit as st
from crypto_jacking import API
import pandas as pd
import global_API
import streamlit as st
import pandas as pd
import time



def update1(URL_search):
    API.call_scan(URL_search)
    st.experimental_rerun()


def page_render(key_value):
    function_tab, file_upload_tab, settings_tab,  = st.tabs(["挖矿脚本筛查", "HTML文件上传", "实时更新"])

    with function_tab:
        URL_search = st.text_input(label = '输入待检测的URL 👇')
        print(URL_search)
        st.write("You entered URL is: ", URL_search)
        st.button("开始筛查", on_click=API.call_scan, args=[URL_search])
        
        if API.flag:
            st.dataframe(pd.DataFrame({'输出信息': API.output_text}), width=700)

            time.sleep(15)
            st.experimental_rerun()
        
             
        else:
            st.write(API.failure_warning)

    with settings_tab:
        settings_file = st.file_uploader("Choose setting file", key=key_value.value())
        API.setting_text = st.text_area(label='setting_text', value=API.update_text, on_change=API.change_update_text, args=[API.setting_text], key=key_value.value())
        update_button_clicked = st.button(label="更新", on_click=API.call_update, key=key_value.value())
        if update_button_clicked:
            st.write(API.advice_text)

    with file_upload_tab:
        uploaded_file = st.file_uploader("Choose a file", key=key_value.value())
        html = uploaded_file.read().decode('utf-8')
        
        if uploaded_file is not None:
            st.button("开始筛查", on_click=API.call_scan, args=[URL_search], key=key_value.value())
            
        #     if API.flag:
        #         st.dataframe(pd.DataFrame({'输出信息': API.output_text}), width=700)
        #     else:
        #         st.write(API.failure_warning)

# threading.Thread(target=Listen).start()
global_API.refresh_by_button(page_render)
