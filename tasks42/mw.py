# -*- coding: utf-8 -*-
from tasks42.models import RequestObject


class SaveHttpRequest(object):
    def process_request(self, request):
        req = RequestObject()
        req.desc = request
        req.remote_address = request.META['REMOTE_ADDR']
        req.save()