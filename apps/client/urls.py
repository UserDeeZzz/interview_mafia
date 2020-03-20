#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: deez
@file: urls.py
@time: 2020/3/20
"""
from django.urls import path
from . import views

app_name = 'apps.client'
urlpatterns = [
    path(r'leader_board', views.LeaderBoardView.as_view(), name='leader_board'), # 排行榜
]
