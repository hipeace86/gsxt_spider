#!/usr/bin/env python
# -*- coding:utf-8 -*-

from task.search.cracker.gsxt_zhejiang_worker import GsxtZheJiangWorker


class GsxtSearchListZheJiangWorker(GsxtZheJiangWorker):
    def __init__(self, **kwargs):
        GsxtZheJiangWorker.__init__(self, **kwargs)

    def get_detail_html_list(self, seed, session, param_list):
        return len(param_list), []
