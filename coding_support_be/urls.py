"""
URL configuration for coding_support_be project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from run_code import views as run_code_view
from explain_code import views as explain_code_view
from action_log import views as action_log_view
from parse_code import views as parse_code_view
from compile_code import views as compile_code_view
from describe_line import views as describe_line_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/run-code/', run_code_view.RunPythonView.as_view()),
    path('api/explain-code/', explain_code_view.ExplainCodeView.as_view()),
    path('api/action-log/', action_log_view.ActionLogView.as_view()),
    path('api/parse-code/', parse_code_view.ParseCodeView.as_view()),
    path('api/compile-code/', compile_code_view.CompileCodeView.as_view()),
    path('api/describe-line/', describe_line_view.DescribeLineView.as_view())
]
