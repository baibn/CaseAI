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

def AIsend(content, session_id):
    payload = json.dumps(
        {"content": content,
         "bot_app_key": "TjcmCrhn",
         "visitor_biz_id": "001",
         "session_id": session_id,
         "visitor_labels": [],
         "streaming_throttle": 100})
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=payload)
    response.encoding = 'utf-8'
    content = extract_reply_content(response.text)
    return content


class AI_client():
    def __init__(self):
        self.end_res = []

    def AIsend_begin_set_play(self, Name, content):
        "根据每种测试方法，发送给AI，分类归纳测试点"
        payload = json.dumps({
            "content": content,
            "bot_app_key": "TjcmCrhn",
            "visitor_biz_id": "001",
            "session_id": "session_%d" % randint(100000, 999999),
            "visitor_labels": [],
            "streaming_throttle": 100})
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        response.encoding = 'utf-8'
        res = extract_reply_content(response.text)
        self.end_res.append(str({'Name': Name, 'res': res}))

    def AIsend_begin_set(self, old_srs, new_srs, srs_case_set):
        "多线程处理"
        ts = []
        for i in range(len(srs_case_set)):
            srs_case_set[i]['AIContent'] += '现在我要分解一段软件开发需求文档，这是我的原始需求：%s。\n' \
                                            '这是我要测试的功能点%s\n。' \
                                            '%s'\
                                            '注意只筛选出哪些功能点或测试点，不要输出测试用例，不要说无关的话，结果用列表存放！' % (old_srs, new_srs,srs_case_set[i])
            ti = threading.Thread(target=self.AIsend_begin_set_play,args=(srs_case_set[i]['Name'], srs_case_set[i]['AIContent']))
            ts.append(ti)
        for t in ts:
            t.start()
        for t in ts:
            t.join()
        return self.end_res