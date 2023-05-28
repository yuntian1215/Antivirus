#开发者：胡余僮
import streamlit as st
from virus_database import API
import global_API
import time

refresh_button = st.sidebar.button('页面更新')
content = st.empty()
key_value = global_API.key_gen()
with content:
    scan_tab, fresh_tab = st.tabs(['邮件扫描', '病毒库更新'])
    with scan_tab:
        scan_Dir = st.text_input(label='扫描路径', value='/mnt/hgfs/share/clamav_test/attach_virus_eml', key=key_value.value())
        scan_button_clicked = st.button("启动扫描", on_click=API.call_scan, args=[scan_Dir], key=key_value.value())

        progress_name = 'progress_counter'
        progress_text = "正在扫描，请稍后......"

        if scan_button_clicked:
            API.scan_output = ''
            print('API.scan_output: ', API.scan_output)
            progress_counter = global_API.create_progress(progress_name)
            progress_counter.start()
        if progress_name in global_API.progress_list:
            progress_counter = global_API.create_progress(progress_name)
            my_bar = st.progress(0, text=progress_text)
            my_bar.progress(progress_counter.value, text=progress_text)
            if API.scan_output != '':
                global_API.clear_progress(progress_name)
                my_bar.progress(100, text='扫描完成')

            st.write(API.scan_output)

    with fresh_tab:
        st.button("更新", on_click=API.call_fresh, key=key_value.value())
        st.write(API.fresh_output)
if refresh_button:
    with content:
        scan_tab, fresh_tab = st.tabs(['病毒库扫描', '病毒库更新'])
        with scan_tab:
            scan_Dir = st.text_input(label='扫描路径', value='/mnt/hgfs/share/clamav_test/attach_virus_eml', key=key_value.value())
            scan_button_clicked = st.button("启动扫描", on_click=API.call_scan, args=[scan_Dir], key=key_value.value())

            progress_name = 'progress_counter'
            progress_text = "正在扫描，请稍后......"

            if scan_button_clicked:
                API.scan_output = ''
                print('API.scan_output: ', API.scan_output)
                progress_counter = global_API.create_progress(progress_name)
                progress_counter.start()
            if progress_name in global_API.progress_list:
                progress_counter = global_API.create_progress(progress_name)
                my_bar = st.progress(0, text=progress_text)
                my_bar.progress(progress_counter.value, text=progress_text)
                if API.scan_output != '':
                    global_API.clear_progress(progress_name)
                    my_bar.progress(100, text='扫描完成')

                st.write(API.scan_output)

        with fresh_tab:
            st.button("更新", on_click=API.call_fresh, key=key_value.value())
            st.write(API.fresh_output)