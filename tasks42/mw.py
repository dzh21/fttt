# -*- coding: utf-8 -*-
from tasks42.models import RequestStr


class SaveHttpRequest(object):
    def process_request(self, request):
        req = RequestStr()
        req.desc = request
        req.save()