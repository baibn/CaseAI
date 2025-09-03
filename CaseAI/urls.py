"""CaseAI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from Myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('get_news/', get_news),
    path('get_projects/', get_projects),
    path('add_project/', add_project),
    path('get_project_detail/', get_project_detail),
    path('update_project_detail/', update_project_detail),
    path('srs_fj/', srs_fj),
    path('save_new_srs/', save_new_srs),
    path('get_old_srs/', get_old_srs),
    path('get_new_srs/', get_new_srs),
    path('optimize_new_srs/', optimize_new_srs),
    path('get_srs_case_set/', get_srs_case_set),
    path('save_set/', save_set),
    path('begin_set/', AIsend_begin_set),

]
