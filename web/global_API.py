import time
import streamlit as st
from threading import Thread


progress_list = {}
class progress(Thread):
    def __init__(self, name=None, estimated_time=10):
        Thread.__init__(self, name=name)
        self.value = 0
        self.estimated_time = estimated_time
        progress_list[name] = self


    def run(self):
        for self.value in range(100):
            time.sleep(self.estimated_time/100)

    def finish(self):
        self.value = 100

def create_progress(name):
    if name not in progress_list:
        print('create progress: ', name)
        return progress(name)
    else:
        print('getting an existing progress: ', name)
        return progress_list[name]

def clear_progress(name):
    del progress_list[name]
