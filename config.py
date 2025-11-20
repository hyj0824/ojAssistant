# -*- coding: utf-8 -*-
"""一些配置与设置"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

USERNAME = "REMOVED"
PASSWORD = "REMOVED"
COOKIES_FILE = os.path.join(BASE_DIR, 'oj_cookies.txt')
WORK_DIRECTORY = ""  # 你的Java作业所在的目录
AUTO_SELECT_COURSE = False
AUTO_SELECT_HOMEWORK = True
MAX_RECORDS_TO_SHOW = 3
