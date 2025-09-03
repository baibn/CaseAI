import json
from django.http import HttpResponse
from django.shortcuts import render
from Myapp.models import *
from openai import OpenAI
from openai import OpenAI, APIError
from Myapp.AIapi import *
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
        # if isinstance(eval(res), list):
        if isinstance(res, list):
            break
        else:
            i += 1
            print("请求失败，正在重试...|重试次数：" + str(i))
    else:
        return HttpResponse(json.dumps(["请求失败，重试次数已达上限。"]), content_type="application/json")
    return HttpResponse(json.dumps(res), content_type="application/json")


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

def get_old_srs(request):
    project_id = int(request.GET['project_id'])
    old_srs = DB_projects.objects.filter(id=project_id)[0].old_srs
    return HttpResponse(json.dumps(old_srs), content_type="application/json")

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
