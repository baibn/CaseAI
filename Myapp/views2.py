import json
import threading
from random import randint

import requests

url = "https://wss.lke.cloud.tencent.com/v1/qbot/chat/sse"

def extract_reply_content(sse_text):
    lines = sse_text.strip().splitlines()
    for line in lines:
        if line.startswith("data:"):
            data_str = line[5:].strip()
            if not data_str:
                continue
            try:
                data = json.loads(data_str)
                if data.get("type") == "reply":
                    content = data["payload"]["content"].strip()
                    return json.loads(content)  # 返回解析后的列表
            except json.JSONDecodeError:
                continue
    return None

class AI_client():
    def __init__(self):
        self.end_res = []
    def AIsend_begin_set_play(self,Name,content):
        payload = json.dumps({
        "content": content,
        "bot_app_key": "TjcmCrhn", # 已欠费，请粉丝自行注册配置AI模型。或咨询粉丝群群主教程。
        "visitor_biz_id": "001",
        "session_id": 'session_%d'%randint(100000,999999),
        "visitor_labels": [],
        "streaming_throttle": 100
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        response.encoding = 'utf-8'
        res = extract_reply_content(response.text)
        self.end_res.append(str({'Name': Name, 'res': res}))
    def AIsend_begin_set(self,old_srs,new_all_content):
        ts = []
        for i in range(len(new_all_content)):
            content = '现在我要对一段软件开发需求文档按照指定的黑盒用例方法来生产测试用例' \
                      '这是我的原始需求：%s。\n' \
                      '这是我要用来生产用例的方法：%s \n' \
                      '这是我要测试的具体功能点列表：%s\n ' \
                      '注意只按照要求的测试方法和要测试的具体功能点写用例，不要写其他功能，不要说其他废话，结果用列表存放！' \
                      % (old_srs, new_all_content[i]['Name'], new_all_content[i]['res'])
            ti = threading.Thread(target=self.AIsend_begin_set_play,args=[new_all_content[i]['Name'],content])
            ts.append(ti)
        for t in ts:
            t.start()
        for t in ts:
            t.join()
        return self.end_res