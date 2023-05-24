import streamlit as st
from virus_database import API

scan_tab, fresh_tab = st.tabs(['病毒库扫描', '病毒库更新'])
with scan_tab:
    scan_Dir = st.text_input(label='扫描路径', value='/mnt/hgfs/share/clamav_test/attach_virus_eml')
    st.button("启动扫描", on_click=API.call_scan, args=[scan_Dir])
    if API.scan_output != '':
        st.write(API.scan_output)

with fresh_tab:
    st.button("更新", on_click=API.call_scan, args=[scan_Dir])


