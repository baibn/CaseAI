import json
import threading
from random import randint

import requests

url = "https://wss.lke.cloud.tencent.com/v1/qbot/chat/sse"


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
    # 按行分割响应内容
    lines = response.text.strip().split('\n')

    # 初始化变量
    contents = []

    # 遍历每一行，解析事件和数据
    for line in lines:
        if line.startswith('data:'):
            # 提取 JSON 数据部分
            data_json = line.split(':', 1)[1].strip()
            try:
                # 解析 JSON 数据
                data = json.loads(data_json)
                # 提取 payload 中的 content 字段
                if 'payload' in data and 'content' in data['payload'] and data['type'] == "reply":
                    contents.append(data['payload']['content'])
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
    return contents[-1]


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
        print(response.text)
        res = json.loads(response.text.split('''event:reply
        data''')[-1])["payload"]["content"]
        self.end_res.append(str({'Name': Name, 'res': res}))

    def AIsend_begin_set(self, old_srs, new_srs, srs_case_set):
        "多线程处理"
        ts = []
        for i in range(len(srs_case_set)):
            srs_case_set[i]['AIContent'] += '现在我要分解一段软件开发需求文档，这是我的原始需求：%s。\n' \
                                            '这是我要测试的功能点%s\n。' \
                                            '注意只筛选出哪些功能点或测试点，不要输出测试用例，不要说无关的话，结果用列表存放！' % (
                                                old_srs, new_srs)
            print(srs_case_set[i]['AIContent'])
            ti = threading.Thread(target=self.AIsend_begin_set_play,
                                  args=(srs_case_set[i]['Name'], srs_case_set[i]['AIContent']))
            ts.append(ti)
        for t in ts:
            t.start()
        for t in ts:
            t.join()
        return self.end_res
