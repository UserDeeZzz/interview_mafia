#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: deez
@file: forms.py
@time: 2020/3/20
"""

from django import forms


class SingleClientForm(forms.Form):
    """
    valid client form
    """
    client = forms.CharField(min_length=4, max_length=10, required=True, error_messages={
        "min_length": "客户端名长度不能小于4",
        "max_length": "客户端名长度不能大于10",
        "invalid": "请输入字符类型的有效客户端名字",
        "required": "客户端名字不能为空",
    })


class LeaderBoardForm(SingleClientForm):
    """
    valid score+client form
    """
    score = forms.IntegerField(max_value=1 << 31 - 1, min_value=0, required=True, error_messages={
        "max_value": "分数不能超过%d" % (1 << 31 - 1),
        "min_value": "分数为正整数",
        "invalid": "分数为小于正整数%d" % (1 << 31 - 1),
        "required": "分数不能为空",
    })


class SearchRankForm(SingleClientForm):
    """
    valid search rank form
    """
    start = forms.IntegerField(min_value=0, required=True,initial=0,error_messages={
        "min_value": "查询起始点必须为自然数",
        "invalid": "查询起始点必须为自然数",
    })

    end = forms.IntegerField(min_value=0, required=True,initial=0,error_messages={
        "min_value": "查询起始点必须为自然数",
        "invalid": "查询起始点必须为自然数",
    })

    def clean(self):
        """
        form.Forms custom interface
        implement custom start&end verification
        :return:
        """
        start = self.cleaned_data['start'] = int(self.cleaned_data.get('start',0))
        end = self.cleaned_data['end'] = int(self.cleaned_data.get('end',0))
        if start > end:
            raise forms.ValidationError(message="查询起始位置应小于等于截止位置")

        return self.cleaned_data