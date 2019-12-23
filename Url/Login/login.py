#_author:leo gao
#encoding:utf-8

import configparser
import os
import json
import random
first = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
case_path = os.path.join(first, "config.ini")
config = configparser.ConfigParser()
config.read(case_path)
ci_url = config.get("url", "backend_url")[1:-1]

login_url = ci_url

