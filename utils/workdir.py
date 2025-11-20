import os
WORK_DIRECTORY = os.getcwd()  # 默认工作目录为当前目录

def get():
    global WORK_DIRECTORY
    return WORK_DIRECTORY

def set(path):
    global WORK_DIRECTORY
    WORK_DIRECTORY = path