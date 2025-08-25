import json
from django.http import HttpResponse
from django.shortcuts import render
from Myapp.models import *
from openai import OpenAI

from openai import OpenAI, APIError

from Myapp.AIapi import *


# # DeepSeek API的URL和认证信息
# DEEPSEEK_API_URL = "https://api.siliconflow.cn/v1"
# MODEL_NAME = "deepseek-ai/DeepSeek-V2.5"
# API_KEY = "sk-egsfijqhpggytleywmeoyeuymzcjdeweszleibtommavsaci"
#
# # 初始化 OpenAI 客户端
# client = OpenAI(api_key=API_KEY, base_url=DEEPSEEK_API_URL)


# def generate_test_features(description):
#     """
#     根据需求描述生成测试功能点。
#
#     :param description: 需求描述字符串
#     :return: 测试功能点列表，如果发生错误则返回空列表
#     """
#     # 参数校验
#     if not description or not isinstance(description, str):
#         return []
#
#     try:
#         # 构造提示词
#         prompt = f'你是一位资深的高级测试工程师，请根据以下需求描述生成测试功能点：{description}，你返回的是一个文本，每个功能点用换行符分隔'
#
#         # 调用 OpenAI API
#         response = client.chat.completions.create(
#             model=MODEL_NAME,
#             messages=[{
#                 "role": "user",
#                 "content": prompt
#             }],
#             temperature=0.7,
#             max_tokens=4096
#         )
#
#         # 提取 content 字段
#         content = response.choices[0].message.content
#
#         # 将 content 按换行符分割成数组
#         test_features = content.strip().split("\n")
#
#         # 返回测试功能点
#         return test_features
#
#     except APIError as e:
#         # 捕获 OpenAI API 错误
#         return []
#     except KeyError as e:
#         # 捕获数据解析错误（例如 response 结构不符合预期）
#         return []
#     except Exception as e:
#         # 捕获其他未知异常
#         return []


# Create your views here.
def get_news(request):
    new_content = DB_News.objects.last()
    return HttpResponse(new_content, content_type="application/json")


def get_projects(request):
    L = list(DB_projects.objects.all().values())
    return HttpResponse(json.dumps(L), content_type="application/json")


def add_project(request):
    name = request.GET.get('name')
    src_case_set = [{"Name": "等价类",
                     "AIContent": "这是一段原始需求和要测试的功能点，请结合原始需求来找出哪些功能点需要做等价类用例设计。"},
                    {"Name": "边界值",
                     "AIContent": "这是一段原始需求和要测试的功能点，请结合原始需求来找出哪些功能点需要做边界值用例设计。"},
                    {"Name": "判定表",
                     "AIContent": "这是一段原始需求和要测试的功能点，请结合原始需求来找出哪些功能点组合(有逻辑关系)需要做判定表用例设计。"},
                    {"Name": "正交法",
                     "AIContent": "这是一段原始需求和要测试的功能点，请结合原始需求来找出哪些功能点组合(无逻辑关系)需要做正交法用例设计"},
                    {"Name": "场景法",
                     "AIContent": "这是一段原始需求和要测试的功能点，请结合原始需求和功能点，来推测出有哪些场景需要做场景法用例设计。"},
                    {"Name": "因果图",
                     "AIContent": "这是一段原始需求和要测试的功能点，请结合原始需求和功能点，来推测出有哪些因果关系需要做场景法用例设计。"},
                    {"Name": "流程图",
                     "AIContent": "这是一段原始需求和要测试的功能点，请结合原始需求和功能点，来推测出有哪些流程(包括主流程、备用流、异常流等)需要做流程法用例设计"},
                    {"Name": "输出域覆盖法",
                     "AIContent": "这是一段原始需求和要测试的功能点，请结合原始需求和功能点，从最终输出或结果的角度，推测出有哪些输出域可以做输出域覆盖法用例设计。"},
                    {"Name": "状态迁移",
                     "AIContent": "这是一段原始需求和要测试的功能点，请结合原始需求和功能点，根据输出或结果状态中可以迁移或改变的关系，推测出有哪些状态需要做状态迁移用例设计"},
                    {"Name": "错误猜测法",
                     "AIContent": "这是一段原始需求和要测试的功能点，请结合原始需求和功能点，统计出有哪些功能点需要做错误猜测法用例设计。"},
                    {"Name": "决策表法",
                     "AIContent": "这是一段原始需求和要测试的功能点，请结合原始需求和功能点，统计出有哪些功能点需要做决策表法用例设计。"},
                    {"Name": "功能图法",
                     "AIContent": "这是一段原始需求和要测试的功能点，请结合原始需求和功能点，统计出有哪些功能点需要做功能图法用例设计。"},
                    {"Name": "比较测试法",
                     "AIContent": "这是一段原始需求和要测试的功能点，请结合原始需求和功能点，统计出有哪些功能点需要做比较测试法用例设计。"},
                    ]
    DB_projects.objects.create(name=name, src_case_set=src_case_set)
    return get_projects(request)


def get_srs_case_set(request):
    project_id = int(request.GET['project_id'])
    srs_case_set = eval(DB_projects.objects.filter(id=int(project_id))[0].src_case_set)
    return HttpResponse(json.dumps(srs_case_set), content_type="application/json")


def get_project_detail(request):
    id = request.GET['id']
    project = list(DB_projects.objects.filter(id=id).values())[0]
    return HttpResponse(json.dumps(project), content_type="application/json")


def update_project_detail(request):
    data = json.loads(request.body)
    DB_projects.objects.filter(id=int(data['id'])).update(**data)
    return HttpResponse('')


def srs_fj(request):
    """需求分解"""
    project_id = int(request.GET['project_id'])
    old_srs = json.loads(request.body)
    content = "分解需求:" + old_srs + '\n请严格按照列表格式回答["功能1","功能2",...]。不要生成测试用例或测试点，不要回答原文没有的功能点，列表之外不要有任何文案，只需原封不动的把这段需求描述分解成若干小功能即可！'
    session_id = "session_" + str(project_id)
    i = 0
    # 重试次数
    while i < 3:
        res = AIsend(content, session_id)
        if isinstance(eval(res), list):
            break
        else:
            i += 1
            print("请求失败，正在重试...|重试次数：" + str(i))
    else:
        return HttpResponse(json.dumps(["请求失败，重试次数已达上限。"]), content_type="application/json")
    return HttpResponse(json.dumps(eval(res)), content_type="application/json")


def optimize_new_srs(request):
    """优化需求"""
    project_id = int(request.GET['project_id'])


def save_new_srs(request):
    project_id = int(request.GET['project_id'])
    DB_new_srs.objects.filter(project_id=project_id).delete()
    new_srs = json.loads(request.body)
    for i in new_srs:
        DB_new_srs.objects.create(content=i, project_id=project_id)
    return HttpResponse('')


def get_new_srs(request):
    project_id = int(request.GET['project_id'])
    new_srs = [i['content'] for i in list(DB_new_srs.objects.filter(project_id=project_id).values('content'))]
    return HttpResponse(json.dumps(new_srs), content_type="application/json")


def save_set(request):
    project_id = int(request.GET['project_id'])
    srs_case_set = json.loads(request.body)
    DB_projects.objects.filter(id=project_id).update(src_case_set=srs_case_set)
    return HttpResponse('')



def AIsend_begin_set(request):
    body = json.loads(request.body)
    old_srs = body['old_srs']
    new_srs = body['new_srs']
    project_id = request.GET['project_id']
    srs_case_set = eval(DB_projects.objects.filter(id=project_id)[0].src_case_set)
    ai_client = AI_client()
    new_srs_end = ai_client.AIsend_begin_set(old_srs, new_srs, srs_case_set)
    return HttpResponse(json.dumps(new_srs_end), content_type="application/json")
